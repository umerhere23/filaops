# Understanding the Dashboard

> Your daily overview of what's happening across your print farm — sales, inventory, production, and what needs your attention right now.

## What You'll Learn

- How to read the Dashboard and what each section tells you
- How to use the Command Center for real-time monitoring
- How to spot problems before they become urgent
- How to navigate from dashboard cards directly to the relevant pages

## The Two Views

FilaOps gives you two ways to monitor your business:

| View | Purpose | Best For |
|------|---------|----------|
| **Dashboard** | Business overview with sales trends and stats | Morning check-in, weekly review |
| **Command Center** | Real-time operational status with action items | During the workday, shift handoffs |

Both are accessible from the sidebar — **Dashboard** is at the top, and **Command Center** is right below it.

---

## Dashboard

Navigate to **Dashboard** in the sidebar (it's the first item). The Dashboard is organized into four sections: Sales, Inventory, Production, and Recent Activity.

<!-- TODO: screenshot of full dashboard -->

### Sales Section

The top of the Dashboard shows a **sales trend chart** and four stat cards.

**Sales Trend Chart**

A line chart showing your revenue over time. Use the period selector in the top-right corner to switch between views:

- **MTD** — Month to date
- **QTD** — Quarter to date
- **YTD** — Year to date
- **Last 30 Days**
- **Last 90 Days**

**Sales Stat Cards**

| Card | What It Shows | Click To Go To |
|------|--------------|----------------|
| **Pending Quotes** | Quotes awaiting customer review | Quotes page |
| **Orders in Progress** | Confirmed + in-production orders | Orders page |
| **Ready to Ship** | Completed orders awaiting shipment (highlights overdue count) | Shipping page |
| **Revenue (30 Days)** | Total revenue and order count for the last 30 days | Payments page |

!!! tip "Color coding"
    Cards turn **red** when something needs attention — for example, the Ready to Ship card turns red if any orders are overdue.

### Inventory Section

Three cards summarize your inventory health:

| Card | What It Shows | Click To Go To |
|------|--------------|----------------|
| **Low Stock Items** | Items below their reorder point or flagged by MRP | Purchasing page (low stock tab) |
| **Active BOMs** | Bill of Materials count and how many need review | Bill of Materials page |
| **Orders Needing Materials** | Orders that require material procurement | Purchasing page |

!!! warning "Low stock matters"
    A green Low Stock card means you're well-stocked. A red card means you have items that could delay production. Click through to see exactly which items need reordering.

### Production Section

A **Production Pipeline** chart shows work orders by status (Draft, Released, Scheduled, In Progress, Complete). Below it, two stat cards summarize:

| Card | What It Shows | Click To Go To |
|------|--------------|----------------|
| **Work Orders In Progress** | Active work orders and how many are ready to start | Production page (filtered to in-progress) |
| **Completed Today** | Units finished today | Manufacturing page |

### Recent Activity

The bottom of the Dashboard shows two side-by-side tables:

**Recent Orders** — Your latest sales orders with customer, product, status, and total. Click any row to open that order.

**Pending Purchases** — Open purchase orders showing vendor, status (Draft or Ordered), item count, total amount, and expected delivery date. Click any row to open that PO.

---

## Command Center

Navigate to **Command Center** in the sidebar. This is your real-time operational view — think of it as your shop floor monitor.

<!-- TODO: screenshot of command center -->

The Command Center auto-refreshes every 60 seconds. You can also click the **Refresh** button in the top-right corner for an immediate update.

### Today's Summary

Four summary cards give you an instant pulse check:

| Card | What It Shows |
|------|--------------|
| **Orders Due Today** | How many orders are due, and how many are ready to ship |
| **Shipped Today** | Orders you've already shipped |
| **In Production** | Active production orders and running operations |
| **Blocked** | Blocked production orders + overdue orders |

!!! warning "Watch the Blocked card"
    If the Blocked card shows a number greater than zero, something needs your immediate attention. Click it to see what's stuck.

### Action Items

The heart of the Command Center. Action items are prioritized alerts that tell you exactly what needs attention:

- **Overdue orders** — Orders past their due date
- **Low stock alerts** — Materials running low
- **Production blocks** — Work orders that can't proceed
- **Pending approvals** — Items waiting for your decision

Each action item shows:

- A **priority indicator** (color-coded)
- A **title** describing the issue
- A **description** with details
- **Suggested actions** you can take

Click any action item to navigate directly to the relevant page.

When everything is handled, you'll see a green **All Clear!** message — your goal for the day.

### Machines

The bottom section shows a **Machine Status Grid** — a visual overview of all your printers and their current state:

- Which machines are **running** (and what they're printing)
- Which machines are **idle** and available
- Which machines are **offline** or need attention

Click any machine to jump to its current production order.

---

## Tips & Best Practices

- **Start your day on the Dashboard** to review sales trends, then switch to the Command Center to plan your work
- **Use the Command Center during the day** — it refreshes automatically and surfaces new issues as they arise
- **Address red items first** — the color coding is designed to draw your eye to problems
- **Click through stat cards** instead of navigating manually — every card links to the relevant page with the right filters applied
- **Check the Command Center before leaving** — the All Clear state means nothing urgent will be waiting for you tomorrow

## What's Next?

Now that you understand your dashboard, learn about the pages you'll navigate to most often:

- [Managing Your Product Catalog](product-catalog.md) — the items you sell and make
- [Taking and Fulfilling Orders](orders.md) — your sales workflow
- [Running Production](production.md) — managing work orders and operations

## Quick Reference

| Task | Where to Find It |
|------|------------------|
| Check today's revenue | **Dashboard** > Sales section > Revenue card |
| See what needs attention | **Command Center** > Action Items |
| Check printer status | **Command Center** > Machines section |
| Find overdue orders | **Dashboard** > Ready to Ship card (red = overdue) |
| View production pipeline | **Dashboard** > Production section > Pipeline chart |
| Check low stock | **Dashboard** > Inventory section > Low Stock card |
| Refresh Command Center | **Command Center** > **Refresh** button (top-right) |
