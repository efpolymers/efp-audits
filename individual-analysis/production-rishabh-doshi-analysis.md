# Operational Documentation: Production Management & Quality Control

## Department Snapshot

### Time & Effort Split
* **Production Scheduling & Operations Planning:** ~25% (estimated)
* **Batch Lot Testing (QC/QI/QA):** ~25% (estimated)
* **Vendor Packaging Negotiation & MOQ Audits:** ~20% (estimated)
* **Inventory Reconciliations & Stock Sheets:** ~15% (estimated)
* **Floor Training & SOP Guidance:** ~15% (estimated) (includes onboarding **4 recent hires**; stated directly)

### Tool Stack
* **Tracking & Warehouse:** Custom Zoho WMS (in-progress), Google Sheets (production, stock, and QC logs)
* **Operational Comms:** WhatsApp, Email

### Key Frequency & Volume Metrics
* **Product Shelf-Life:** **3 years** (stated directly)
* **Packaging MOQ Overrun Example:** **16,000** printed pouches for **5,000** unit orders → **11,000 (68%)** surplus pouches stored (stated directly)
* **Hiring Volume:** **4** new production personnel onboarded recently (stated directly)
* **Stock Reporting Cadence:** Weekly stock valuation sheets shared with Accounts (stated directly)

### Red Flags
1. **High**: *Surplus Custom Packaging Risk* — Custom pouch MOQs (e.g., 16,000 pouches minimum print run) result in major warehouse surplus and write-off exposure when clients revise packaging designs.
2. **High**: *Siloed Zoho WMS Database* — The custom Zoho WMS is disconnected from the main Zoho Books ERP, requiring manual reconciliation for cost auditing and margin calculations.
3. **Medium**: *Absence of Sales Packaging Forecasts* — Sales teams provide custom packaging specs only at order intake. This removes the lead time buffer needed to coordinate printer runs, causing production blockages.
4. **Low**: *Finished Goods Expiry Exposure* — A premium pricing strategy prevents discounted stock liquidation, creating expiration write-off risks for finished goods held in slow-moving export lanes (3-year shelf life).

---

## 1. Operational Profile & Scope
* **Department/Business Unit:** Production — manages chemical formulation, product granulation, packaging lines, warehouse storage, quality inspections, and machine procurement.
* **Core Production Strategy:** "Produce to Stock, Stock to Pack, then Dispatch." Primary manufacturing converts raw materials into bulk semi-finished goods (SFG) for inventory storage. Packaging is executed as a secondary step against specific client sales orders.
* **Key Focus:** Managing product quality standards, raw material yields, and container dispatch preparation.

---

## 2. Team Structure & Quality Split

### Personnel Roles & KPIs
Led by Production Manager Rishabh Doshi, the department manages Udaipur and Coimbatore factory operations:
* **Production Manager (Rishabh Doshi):** Directs plant operations, coordinates capex machinery procurement, manages vendor relations, and oversees labor compliance.
* **Production Executive (Harshit Sharma - Factory Udaipur):** Manages Udaipur daily production schedules, raw material intake, packaging runs, and floor labor.
* **QC Executive (Khyati Poonia - Factory Udaipur):** Executes laboratory testing, material inspection, and batch release certification.

### Quality Control Split
Quality checking is structured into three specialized stages:
* **Quality Checking (QC):** Verifying specifications of incoming raw materials before warehouse intake.
* **Quality Inspection (QI):** Inspecting dimensions, seal integrity, and printing alignment of packaging pouches and boxes.
* **Quality Assessment (QA):** Scientific testing of physical granule sizes and hydration absorption rates of finished batches.

### Effort & Time Allocation
* **Production Scheduling & Operations Planning:** ~4–6 hours/week (inferred from coordinating sales demands and raw material capacity).
* **Vendor Packaging Negotiation & MOQ Audits:** ~5–8 hours/week (inferred from coordinating mockups and balancing printer MOQs).
* **Inventory Reconciliation & Stock Sheet Compilation:** ~4–6 hours/week (inferred from preparing manual stock valuations for Accounts).
* **Batch Lot Testing (QC/QI/QA):** ~1.5–2.5 hours/day (inferred from testing incoming raw materials and finished goods).
* **Floor Training & SOP Guidance:** ~3–5 hours/week (inferred from on-the-job training of **4 recent additions** with **~1 year** tenure).

---

## 3. Product Matrix & Variation Complexity
The manufacturing line manages a multi-variable product matrix:
1. **Granule Size Range:**
   * **India Market:** Finer size (<2mm range) for manual broadcasting by farmers (stated directly).
   * **International Markets:** Coarser sizes (e.g., 2–4mm, or precise bands like 1.18–1.41mm) for mechanized agricultural application (stated directly).
2. **SKU Capacities:** Spans 50g, 100g, 200g, 500g, 1kg, and 5kg bags, up to 20-25kg, 100kg, and bulk sacks (1,000–1,400kg).
3. **Packaging Language Variants:** Text and legal labeling in Hindi, English, Spanish, French, Japanese, etc.

---

## 4. Inventory Management & Zoho WMS
* **Storage Categories:** Raw Material (stored in 50kg sacks); Semi-Finished Goods (SFG; stored in 50kg or 100kg intermediate bulk containers); Finished Goods (packaged SKU formats ready for dispatch).
* **Fulfillment Protocol:** Inventory rotation follows First-In, First-Out (FIFO) guidelines. A minimum inventory policy is maintained to protect against variable sales lead times.
* *Refer to the Tool Stack in the snapshot at the top of this report for WMS system details.*

---

## 5. Packaging Procurement & MOQ Friction

### Printer MOQ Cost Dynamics
Packaging vendors enforce high Minimum Order Quantities (MOQs) for custom-branded print runs:

```
[Sales Request: 5,000 custom B2B pouches]
                    |
[Printer Minimum Constraint: 16,000 pouch MOQ]
                    |
                    +--> Production prints 16,000 pouches (MOQ threshold)
                    +--> 5,000 pouches filled & shipped immediately
                    +--> 11,000 surplus pouches stored as inventory risk
```

* **Excess Inventory Accumulation:** Print-run constraints force the procurement of excess custom pouches. The surplus (e.g., **11,000 pouches** in the example above, stated directly) is stored in the warehouse. If a client design changes, these pouches must be written off.
* **Coordination Loop:** When custom orders arrive, Production checks existing warehouse pouch inventories. If inventory is depleted, Production coordinates print costs and timings with Sales before execution.

---

## 6. Quality Control & Shelf-Life Policies
* **Batch Lot-Testing:** Every raw material batch is date-coded. QC testing must be completed and logged before material is released to processing lines.
* **Shelf-Life Constraints:** Finished products carry a **3-year shelf life** (stated directly).
* **Brand Protection:** To preserve premium market pricing in export regions, EFP does not discount or dump aging inventory. Aging finished stocks are tracked to ensure rotation before expiration.

---

## 7. Cross-Department Dependencies

| Target Department | Nature of Dependency | Frequency / Impact |
|---|---|---|
| **Sales & BD** | Requests for lead times and confirmation of stock availability. | Daily / High frequency |
| **Logistics** | Dispatch coordination, container booking schedules, and packing lists. | Daily |
| **Accounts** | Providing weekly stock sheets for inventory valuation and margin audits. | Weekly |
| **R&D** | Aligning chemical formulations and testing new product variants. | Project-based |

---

## 8. Operational Friction & Bottlenecks (Audit Analysis)
*Documented under the Red Flags section at the top of this report.*

---

## 9. Audit Backlog & Follow-Up Items
* **Custom Zoho WMS Audit:** Review the architecture and data tables of the custom Zoho WMS to check for compatibility with Zoho Books.
* **Factory Alignment Audit:** Compare Udaipur and Coimbatore factory production lines to verify consistency in SOPs and QC tracking methods.
* **Packaging MOQ Financial Analysis:** Audit historical pouch write-offs caused by B2B design updates to evaluate the cost-impact of custom order profiles.
