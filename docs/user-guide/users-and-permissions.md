# Users and Permissions

> Control who can access FilaOps and what they can do.

## What You'll Learn

- How to add and manage team members
- The difference between Admin and Operator roles
- How to reset passwords and deactivate accounts
- How to run a security audit on your installation

## Prerequisites

- Admin access to FilaOps (Operators cannot manage users)

---

## Understanding Roles

FilaOps has two user roles:

| Role | Access Level | Typical User |
|------|-------------|--------------|
| **Admin** | Full access to all features including settings, users, and accounting | Business owner, office manager |
| **Operator** | Production floor access — orders, production, inventory, printers | Print technician, warehouse staff |

Operators can view and work with day-to-day operational features but cannot access administration pages like settings, user management, or accounting.

---

## Managing Team Members

Navigate to **Settings > Team Members** in the sidebar.

<!-- TODO: screenshot of team members page -->

### Overview

The page shows summary cards at the top:

- **Total Active** — Number of currently active users
- **Admins** — Count of users with Admin role
- **Operators** — Count of users with Operator role
- **Inactive** — Count of deactivated accounts

### Finding Users

Use the controls above the table to find specific users:

- **Search** — Type a name or email address to filter the list
- **Role filter** — Select **All Roles**, **Admin**, or **Operator** to filter by role
- **Show Inactive** — Check this box to include deactivated accounts in the list

### The User Table

| Column | What It Shows |
|--------|--------------|
| **User** | Name and avatar |
| **Email** | Login email address |
| **Role** | Admin (purple badge) or Operator (blue badge) |
| **Status** | Active (green), Inactive (gray), or Suspended (red) |
| **Last Login** | When the user last signed in, or "Never" |
| **Actions** | Edit, reset password, or deactivate |

---

## Adding a Team Member

**Step 1.** Click **+ Add Member**.

**Step 2.** Fill in the required fields:

| Field | Required | Notes |
|-------|----------|-------|
| **Email** | Yes | Must be unique — this is the login username |
| **Temporary Password** | Yes | Minimum 8 characters. The user should change this on first login. |
| **First Name** | No | Displayed in the user list and navigation bar |
| **Last Name** | No | Displayed in the user list |
| **Role** | Yes | Choose **Admin** or **Operator** |

**Step 3.** Click **Create** to save.

Share the email and temporary password with your new team member so they can sign in.

!!! tip "Choosing the right role"
    Start new users as **Operators** unless they specifically need access to settings, accounting, or user management. You can always upgrade their role later.

---

## Editing a Team Member

**Step 1.** Find the user in the table and click the **Edit** (pencil) button.

**Step 2.** Update any fields — email, name, role, or status.

**Step 3.** Click **Save Changes**.

!!! warning "Changing roles"
    Changing a user from Admin to Operator immediately removes their access to administration pages. Make sure at least one Admin account remains active.

---

## Resetting a Password

If a team member forgets their password or you need to force a password change:

**Step 1.** Find the user in the table and click the **Reset Password** button.

**Step 2.** Enter a new password (minimum 8 characters), or click **Generate random password** to create a secure 12-character password automatically.

**Step 3.** Click **Reset Password** to confirm.

!!! warning "Session invalidation"
    Resetting a password immediately invalidates all of that user's active sessions. They will be signed out everywhere and must log in again with the new password.

**Step 4.** Share the new password with the user through a secure channel.

---

## Deactivating and Reactivating Users

### Deactivating

When someone leaves your team or no longer needs access:

**Step 1.** Find the user in the table.

**Step 2.** Click the **Deactivate** button.

The user's status changes to **Inactive** and they can no longer sign in. Their account and history are preserved — deactivation is not deletion.

### Reactivating

To restore a previously deactivated account:

**Step 1.** Check **Show Inactive** to reveal deactivated accounts.

**Step 2.** Find the user and click **Reactivate**.

The user's status returns to **Active** and they can sign in again with their existing password.

---

## Security Audit

Navigate to **Settings > Security** in the sidebar. The security audit scans your FilaOps installation and flags potential configuration issues.

<!-- TODO: screenshot of security audit page -->

### Running an Audit

The audit runs automatically when you open the page. Click **Refresh** to re-run it at any time.

### Reading the Results

The top of the page shows an overall status:

| Status | Meaning |
|--------|---------|
| **All Clear** (green) | All checks passed — your installation is well-configured |
| **Warnings Found** (yellow) | Some checks flagged potential issues worth reviewing |
| **Action Required** (red) | Critical issues that should be addressed |

Below the status, summary cards show the count of **Passed**, **Warning**, and **Failed** checks.

### Check Categories

Checks are organized by severity:

- **Critical** (red) — Security issues that should be fixed immediately, such as using default passwords or missing HTTPS
- **Warning** (yellow) — Improvements recommended, such as enabling rate limiting or configuring backups
- **Informational** (blue) — Status information that doesn't require action

Each check shows:

- **Name** — What was checked
- **Status** — Pass, Fail, or Warning
- **Message** — Explanation of the result
- **Remediation** — For failed checks, a **Fix This** button with instructions on how to resolve the issue

### Common Security Checks

| Check | What It Verifies |
|-------|-----------------|
| Secret key not default | Your application secret key has been changed from the default value |
| Secret key entropy | Your secret key is sufficiently random and long |
| HTTPS enabled | Your installation is served over HTTPS |
| CORS not wildcard | Cross-origin settings are restricted to specific domains |
| Admin password changed | The default admin password has been changed |
| Rate limiting enabled | API rate limiting is active to prevent abuse |
| Backup configured | Database backups are set up |

### Exporting the Report

Click **Export Report** to download the full audit results as a JSON file. This is useful for compliance documentation or sharing with your IT team.

---

## Tips and Best Practices

- **Change the default admin password immediately** — The security audit will flag this if you haven't. Use a strong, unique password.
- **Use individual accounts** — Don't share login credentials between team members. Each person should have their own account for accountability and audit trails.
- **Review the security audit monthly** — Run the audit after any system changes (updates, new server configuration, etc.) to catch new issues.
- **Keep at least two Admin accounts** — If your primary admin forgets their password, a second admin can reset it. A single admin account is a single point of failure.
- **Deactivate, don't delete** — When someone leaves, deactivate their account. This preserves their activity history in your system.

## What's Next?

- [System Settings](system-settings.md) — configure company information, tax rates, and business hours
- [Installation and Setup](installation.md) — server configuration that affects security checks
- [Your First Day](first-day.md) — initial setup including creating your first admin account

## Quick Reference

| Task | Where to Find It |
|------|-------------------|
| View team members | **Settings** > **Team Members** |
| Add a new user | **Settings** > **Team Members** > **+ Add Member** |
| Change a user's role | **Settings** > **Team Members** > **Edit** on the user row |
| Reset a password | **Settings** > **Team Members** > **Reset Password** on the user row |
| Deactivate an account | **Settings** > **Team Members** > **Deactivate** on the user row |
| Run security audit | **Settings** > **Security** |
| Export security report | **Settings** > **Security** > **Export Report** |
