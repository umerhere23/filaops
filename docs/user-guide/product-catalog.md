# Managing Your Product Catalog

> Your product catalog is the foundation of FilaOps — every order, production run, and inventory count ties back to items defined here.

## What You'll Learn

- How to create and organize items (products, materials, components, supplies)
- How to use categories to keep your catalog tidy
- How to build Bills of Materials (BOMs) for manufactured products
- How to set up manufacturing routings
- How to recost your catalog when material prices change

## Prerequisites

- Admin access to FilaOps
- At least one location set up (see [System Settings](system-settings.md))

---

## Understanding Item Types

Every item in FilaOps has a type that determines how the system treats it:

| Type | What It Is | Example |
|------|-----------|---------|
| **Finished Good** | A product you sell to customers | Custom phone case, Miniature figurine |
| **Component** | A part used in manufacturing but not sold directly | 3D-printed bracket, Insert nut |
| **Material** | Raw material consumed during production | PLA filament, Resin |
| **Supply** | Consumable supplies for operations | Glue stick, Masking tape, Build plate |

!!! tip "Choosing the right type"
    If a customer can order it, it's a **Finished Good**. If it goes into a finished good, it's a **Component**. If it's consumed by a printer, it's a **Material**. Everything else is a **Supply**.

---

## The Items Page

Navigate to **Inventory > Items** in the sidebar. This is your main catalog management page.

<!-- TODO: screenshot of items page -->

### Page Layout

- **Left sidebar** — Category tree for filtering items by category
- **Top bar** — Search, filters (item type, active/inactive), and view toggle (table or cards)
- **Main area** — Your item list with stock status, quantities, costs, and prices
- **Quick filter pills** — Filter by type (Finished Goods, Components, Materials, Supplies) or show only items that need reordering

### View Modes

Toggle between two views using the icons in the top-right:

- **Table view** — Spreadsheet-style list with sortable columns. Best for managing many items at once.
- **Card view** — Visual cards sorted by stock status (shortages first). Best for a quick visual scan.

### Stock Status Colors

Items are color-coded by inventory health:

| Color | Meaning |
|-------|---------|
| **Red** | Shortage — available quantity is negative |
| **Orange** | Out of Stock — nothing available |
| **Yellow** | Low Stock — less than 20% of on-hand quantity available |
| **Green** | In Stock — healthy inventory levels |

---

## Creating an Item

**Step 1.** Click **+ New Item** (for products, components, or supplies) or **+ New Material** (for filament and other raw materials).

**Step 2.** Fill in the item details:

- **Name** — What you call this item (e.g., "Dragon Figurine - Red PLA")
- **SKU** — Your internal part number (optional but recommended)
- **Item Type** — Finished Good, Component, Material, or Supply
- **Category** — Which category this item belongs to
- **Unit of Measure** — How you count this item (each, gram, kilogram, meter, etc.)
- **Reorder Point** — The quantity at which you want to be alerted to reorder
- **Standard Cost** — How much it costs you to make or buy this item
- **Selling Price** — How much you charge customers (for Finished Goods)

**Step 3.** Click **Save**.

!!! info "Materials are special"
    When you click **+ New Material**, you get additional fields for material properties like material type, color, and manufacturer. This helps with traceability and spool tracking.

### Editing an Item

Click any item in the list to open its detail view. Make your changes and click **Save**.

### Deactivating an Item

Instead of deleting items (which could break historical order records), deactivate them. Edit the item and toggle the **Active** switch off. Deactivated items won't appear in searches or order forms but remain in your records.

---

## Organizing with Categories

Categories help you group related items. You can create a hierarchy of categories (e.g., "Filament > PLA > Silk PLA").

### Creating a Category

**Step 1.** In the category sidebar on the left, click the **+** button.

**Step 2.** Enter the category name.

**Step 3.** Optionally select a **Parent Category** to nest it under an existing category.

**Step 4.** Click **Save**.

### Filtering by Category

Click any category in the left sidebar to show only items in that category. Click it again (or click **All Items**) to remove the filter.

---

## Bills of Materials (BOMs)

A BOM defines what goes into making a product — the list of materials and components, their quantities, and optional scrap factors.

Navigate to **Inventory > Bill of Materials** in the sidebar.

<!-- TODO: screenshot of BOM page -->

### Creating a BOM

**Step 1.** Click **+ New BOM**.

**Step 2.** Select the **Product** — the finished good or component this BOM produces.

**Step 3.** Add **BOM Lines** — each line specifies:

- The **component or material** consumed
- The **quantity per unit** produced
- An optional **scrap factor** (percentage expected to be wasted)

**Step 4.** Click **Save**.

### BOM Detail View

Click any BOM in the list to see its full details, including:

- All component lines with quantities
- The calculated cost based on component standard costs
- A visual component breakdown

### Actions from the BOM Page

| Action | What It Does |
|--------|-------------|
| **Copy BOM** | Duplicates a BOM — useful when creating variants |
| **Create Production Order** | Launches a production order directly from this BOM |
| **Delete BOM** | Removes the BOM (only if no production orders reference it) |

!!! tip "Quote-to-BOM workflow"
    When you accept a quote, FilaOps can link directly to the BOM page for the quoted product. You'll see the quoted quantity pre-filled when creating the production order.

---

## Manufacturing Routings

A routing defines the sequence of operations needed to produce an item — which machines to use, how long each step takes, and the order of operations.

### Setting Up a Routing

**Step 1.** Open an item and click **Edit Routing**.

**Step 2.** Add operations in sequence:

- **Operation name** — What this step is called (e.g., "Print", "Post-Process", "Assembly")
- **Work center / Machine** — Which printer or workstation handles this step
- **Setup time** — Time to prepare the machine (in minutes)
- **Run time** — Time per unit produced (in minutes)

**Step 3.** Click **Save**.

Routings feed into production scheduling and help FilaOps estimate when orders will be ready.

---

## Bulk Operations

### Bulk Update

**Step 1.** Select multiple items using the checkboxes in table view.

**Step 2.** Click **Bulk Update** in the toolbar that appears.

**Step 3.** Choose which field to update (category, active status, reorder point, etc.) and the new value.

**Step 4.** Click **Apply** to update all selected items at once.

### Recost All Items

When material prices change, you can recalculate all item costs at once:

**Step 1.** Click the **Recost** button in the page header.

**Step 2.** Confirm the action. FilaOps will walk through every BOM and update standard costs based on current component prices.

**Step 3.** Review the results showing how many items were updated and the cost changes.

!!! warning "Recost affects pricing"
    Recosting updates standard costs throughout the system. Existing orders aren't affected, but new quotes and orders will use the updated costs. Review the results carefully.

---

## Importing Items

If you have an existing product list, you can import items from a CSV file.

### Import Materials

Navigate to **Inventory > Import Materials** in the sidebar. This page lets you bulk-import materials from supported filament databases and CSV files.

### CSV Import (from Onboarding)

During initial setup, the onboarding wizard offers CSV import for products, customers, and inventory. You can also access order import later via **Admin > Import Orders**.

---

## Tips & Best Practices

- **Set reorder points** on every material and supply — this powers the Low Stock alerts on your Dashboard
- **Use consistent naming** — "PLA Black 1kg Spool" is better than "black pla" for searchability
- **Create categories early** — it's easier to organize 10 items into categories than 500
- **Review BOMs after recosting** — make sure updated costs look reasonable before creating new quotes
- **Keep SKUs unique** — if you use SKUs, make sure no two items share the same one

## What's Next?

With your catalog set up, you're ready to start selling:

- [Taking and Fulfilling Orders](orders.md) — create quotes and sales orders
- [Tracking Inventory](inventory.md) — manage stock levels and transactions
- [Running Production](production.md) — manufacture items from your BOMs

## Quick Reference

| Task | Where to Find It |
|------|------------------|
| Create a new product | **Inventory > Items** > **+ New Item** |
| Create a new material | **Inventory > Items** > **+ New Material** |
| Set up a BOM | **Inventory > Bill of Materials** > **+ New BOM** |
| Edit a routing | Open an item > **Edit Routing** |
| Import materials | **Inventory > Import Materials** |
| Recost all items | **Inventory > Items** > **Recost** button |
| Bulk update items | Select items with checkboxes > **Bulk Update** |
| Create a category | **Inventory > Items** > Category sidebar > **+** button |
| Filter by category | Click a category in the left sidebar |
| Switch to card view | Click the card icon in the top-right of the Items page |
