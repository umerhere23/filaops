# Monitoring Your Printers

> Track every printer on your floor — status, maintenance, and active jobs at a glance.

## What You'll Learn

- How to add and configure printers in FilaOps
- How to monitor printer status and active print jobs
- How to track maintenance schedules and service history
- How to discover networked printers automatically
- How to bulk-import printers from CSV

## Prerequisites

- Admin access to FilaOps
- At least one work center set up (see [Running Production](production.md))
- Printer IP addresses (for network-connected printers)

---

## The Printers Page

Navigate to **Printers** in the sidebar. The page has four tabs across the top:

- **All Printers** — Your complete fleet with live status (shows a count badge)
- **Maintenance** — Service schedules and history (shows an overdue count badge when maintenance is due)
- **Network Discovery** — Scan your network for connected printers
- **CSV Import** — Bulk-add printers from a spreadsheet

<!-- TODO: screenshot of printers page -->

---

## Your Printer Fleet

The **All Printers** tab displays your printers in a card grid layout — three cards per row, each showing the key details about one printer.

### Reading a Printer Card

Each card shows:

- **Printer Name** — The name you've given this machine
- **Printer Code** — Your internal identifier
- **Status Badge** — Color-coded current state:

| Status | Color | Meaning |
|--------|-------|---------|
| **Idle** | Green | Online and ready for work |
| **Printing** | Blue | Currently running a print job |
| **Offline** | Gray | Not reachable or powered off |
| **Error** | Red | Reporting a problem that needs attention |

- **Brand and Model** — The manufacturer and model number
- **IP Address** — The network address (if connected)
- **Location** — Where the printer is physically located
- **Capability Badges** — Tags showing special features:
    - **AMS** — Automatic Material System (multi-color)
    - **Camera** — Has a built-in camera for remote monitoring
    - **Enclosure** — Has an enclosed build chamber

When a printer is actively working, the card also shows:

- **Active Job** — The name of the current print job
- **Progress** — A progress bar with percentage complete

!!! info "Live status updates"
    FilaOps polls your printers for active work every 30 seconds. Progress bars update automatically — no need to refresh the page.

### Filtering Your Fleet

Use the controls above the card grid to find specific printers:

- **Search** — Find printers by name, code, or other details
- **Brand dropdown** — Show only printers from a specific manufacturer
- **Status dropdown** — Show only printers in a specific state (Idle, Printing, Offline, Error)

### Adding a Printer

**Step 1.** Click **+ Add Printer**.

**Step 2.** Fill in the printer details:

- **Printer Name** — A descriptive name (e.g., "Prusa MK4 #3") (required)
- **Printer Code** — Your internal shorthand (e.g., "MK4-03")
- **Brand** — The manufacturer
- **Model** — The specific model
- **Serial Number** — The manufacturer's serial number
- **IP Address** — The printer's network address (for status polling)
- **Location** — Which physical location this printer is at
- **Status** — Current operational state
- **Capabilities** — Check the boxes for AMS, Camera, and/or Enclosure
- **Notes** — Any additional details (firmware version, special configuration, etc.)

**Step 3.** Click **Save**.

### Testing Connectivity

Click **Test All** at the top of the page to check the network connection to every printer in your fleet at once. This verifies that FilaOps can reach each printer's IP address and reports any that are unreachable.

<!-- TODO: screenshot of printer card with active job -->

---

## Maintenance Tracking

The **Maintenance** tab helps you stay on top of preventive maintenance so your printers don't fail mid-print. If any printers have overdue maintenance, the tab shows an orange badge with the count.

<!-- TODO: screenshot of maintenance tab -->

### Maintenance Due Summary

At the top of the tab, a summary section shows which printers are due or overdue for service. Each entry shows the printer name, what type of maintenance is needed, and when it was last performed.

### Logging Maintenance

When you perform maintenance on a printer:

**Step 1.** Select the printer from the dropdown.

**Step 2.** Fill in the maintenance record:

- **Maintenance Type** — What kind of service was performed (e.g., "Nozzle Replacement," "Belt Tension," "Lubrication")
- **Description** — Details about what was done
- **Cost** — Parts and labor cost for this service
- **Downtime (hours)** — How long the printer was out of service

**Step 3.** Click **Log Maintenance**.

### Maintenance History

Below the form, a history table shows all past maintenance records for the selected printer:

| Column | What It Shows |
|--------|--------------|
| **Date** | When the maintenance was performed |
| **Type** | What kind of service was done |
| **Description** | Details about the work |
| **Cost** | How much it cost |
| **Downtime** | How long the printer was offline |

!!! tip "Schedule regular maintenance"
    Set up a monthly cadence for routine maintenance — nozzle checks, belt tension, bed leveling, lubrication. Catching small issues early prevents mid-print failures that waste filament and time.

---

## Network Discovery

The **Network Discovery** tab lets you scan your local network to find printers automatically, rather than manually entering IP addresses one at a time.

<!-- TODO: screenshot of network discovery tab -->

### How Discovery Works

FilaOps uses two methods to find printers on your network:

1. **IP Range Probe** — Scans a range of IP addresses looking for devices that respond on common printer ports
2. **SSDP/mDNS** — Listens for printers that broadcast their presence using standard discovery protocols (like Bonjour)

### Running a Discovery Scan

**Step 1.** Enter the IP range to scan (e.g., `192.168.1.1` to `192.168.1.254`).

**Step 2.** Click **Discover**.

**Step 3.** Review the results — each discovered device shows its IP address, hostname (if available), and any identifying information.

**Step 4.** For each printer you want to add, click **Add** to create a new printer record pre-filled with the discovered IP address.

!!! info "Discovery scope"
    Network discovery only finds printers on your local network segment. If your printers are on a different subnet or VLAN, you'll need to enter their IP addresses manually.

---

## CSV Import

If you're setting up a new print farm or migrating from another system, you can import your entire fleet from a CSV file instead of adding printers one at a time.

<!-- TODO: screenshot of CSV import tab -->

### Import Format

Your CSV file should include columns for the printer details. At minimum, include:

- **Name** — The printer name (required)
- **Code** — Your internal identifier
- **Brand** — Manufacturer name
- **Model** — Model number
- **IP Address** — Network address
- **Location** — Physical location
- **Serial Number** — Manufacturer serial

### Running an Import

**Step 1.** Prepare your CSV file with the columns listed above.

**Step 2.** Click **Choose File** and select your CSV.

**Step 3.** Map your CSV columns to FilaOps fields if the column names don't match automatically.

**Step 4.** Review the preview to make sure the data looks correct.

**Step 5.** Click **Import** to create all printer records at once.

---

## Tips & Best Practices

- **Assign meaningful names** — "Prusa MK4 #3 - Left Rack" is much more useful than "Printer 3" when you're troubleshooting across a room full of machines
- **Keep IP addresses current** — If your printers use DHCP, consider setting static IPs or DHCP reservations so FilaOps can always reach them
- **Tag capabilities accurately** — The AMS, Camera, and Enclosure badges help you assign the right jobs to the right printers
- **Log every maintenance event** — Even quick fixes like clearing a jam. Over time, the maintenance history reveals which printers are reliable and which are trouble
- **Track downtime costs** — Recording the cost and downtime of each repair helps you decide when to replace a printer instead of fixing it again
- **Use network discovery on setup day** — When commissioning a new farm, run a discovery scan instead of typing in 20 IP addresses manually
- **Monitor the overdue badge** — If the Maintenance tab shows a count, printers are past their service interval. Don't wait for a failure

## What's Next?

With your printers configured and monitored, you can put them to work:

- [Running Production](production.md) — assign production orders to your printers via work centers
- [Material Planning (MRP)](mrp.md) — plan material needs based on your production schedule
- [Tracking Inventory](inventory.md) — track filament spools loaded on each printer

## Quick Reference

| Task | Where to Find It |
|------|-----------------|
| View all printers | **Printers** > **All Printers** tab |
| Add a printer | **Printers** > **+ Add Printer** |
| Check printer status | **Printers** > Look at status badges on printer cards |
| Test connectivity | **Printers** > **Test All** button |
| Log maintenance | **Printers** > **Maintenance** tab > Fill form > **Log Maintenance** |
| Check overdue maintenance | **Printers** > **Maintenance** tab > Look for overdue badge |
| Discover network printers | **Printers** > **Network Discovery** tab > **Discover** |
| Import printers from CSV | **Printers** > **CSV Import** tab > Upload file > **Import** |
