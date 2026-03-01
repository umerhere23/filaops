#!/bin/bash
# docker-entrypoint.sh — Container startup script.
# Handles PRO plugin auto-download and starts the application.
#
# Flow:
#   1. If FILAOPS_LICENSE_KEY is set and filaops-pro not installed → download + install
#   2. Drop to non-root user and start uvicorn
#
# This runs at container START (every time), not at build time.
# No Docker rebuild needed to add or remove PRO.

set -e

# ─── PRO Plugin Auto-Download ───
# If a license key is set, ensure filaops-pro is installed.
# Downloads from the license server using the key for auth.
if [ -n "$FILAOPS_LICENSE_KEY" ]; then
    if ! python -c "import filaops_pro" 2>/dev/null; then
        echo "FilaOps: License key detected. Downloading PRO plugin..."
        LICENSE_URL="${LICENSE_SERVER_URL:-https://license.blb3dprinting.com}"
        WHEEL_PATH="/tmp/filaops_pro.whl"

        if curl -sf -H "X-License-Key: $FILAOPS_LICENSE_KEY" \
            "$LICENSE_URL/api/v1/download/filaops-pro" \
            -o "$WHEEL_PATH"; then
            pip install --no-cache-dir "$WHEEL_PATH" 2>&1 | tail -1
            rm -f "$WHEEL_PATH"
            echo "FilaOps: PRO plugin installed."
        else
            echo "FilaOps: Could not download PRO plugin. Check your license key."
            echo "FilaOps: Starting in Community mode."
        fi
    fi
fi

# ─── Start Application ───
# Drop to non-root user for the application process
exec su -s /bin/bash appuser -c "uvicorn app.main:app --host 0.0.0.0 --port 8000"
