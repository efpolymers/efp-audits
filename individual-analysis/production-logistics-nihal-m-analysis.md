# Operational Documentation: Production & Logistics

## Department Snapshot

### Time & Effort Split
* **Carrier Coordination & Scheduling:** ~35% (estimated)
* **Documentation & Billing (Invoice/E-Way Bill):** ~30% (estimated)
* **Physical Loading & Stuffing Supervision:** ~20% (estimated)
* **Exception Chasing & Data Validation:** ~15% (estimated)
* **Manager's Comms Overhead:** Stated directly as **10%** of effort for small orders; **30%** for large/complex dispatches.

### Tool Stack
* **Tracking & Databases:** Manual Excel/Google Sheets (primary logistics and dispatch sheets)
* **Invoicing & Accounts:** Zoho Books
* **Operational Comms:** WhatsApp (dominant; dedicated sales and carrier groups), Email, Slack

### Key Frequency & Volume Metrics
* **Vessel Cut-off Buffer:** **2–4 days** ahead of container stuffing (stated directly)
* **Export Container Preparation SLA (20ft):** **1 week** (stated directly)
* **Logistics Call Duration:** **10–15 minutes** per small order; **20–25 minutes** per large order (stated directly)
* **Manual Production Turnaround (e.g., 2 MT):** **10 days** (stated directly)
* **Logistics Team Scale:** **2** full-time personnel (stated directly)

### Red Flags
1. **High**: *Disconnected Invoicing & Shipping Sheets* — Zoho Books and the logistics tracking sheet operate as separate, disconnected databases, requiring manual double-entry.
2. **High**: *Incomplete WhatsApp Order Intake* — Sales orders are entered via WhatsApp text with missing fields (pin codes, SKU weight), causing shipment delays.
3. **Medium**: *Ocean Freight Schedule Shifts* — Vessel schedule shifts and cutoff delays require manual tracking and notification, introducing export delays.
4. **Low**: *Factory Single-Line Capacity* — The Coimbatore plant runs a single production line, meaning peak export shipments delay domestic orders.

---

## 1. Operational Profile & Scope
* **Department/Business Unit:** Production (Logistics) — manages domestic and international product dispatches, freight booking, customs documentation, and inventory movements.
* **Team Structure & Roles:**
  * **Logistics Manager (Nihal Paliwal):** Leads carrier negotiations, coordinates international customs clearances, plans shipping schedules, and manages client escalations.
  * **Logistics Executive (Surajmal Khatik):** Handles physical warehouse dispatches, logs loading sheets, and monitors domestic transit status.
* **Scope of Activity:** Coordinates primary freight (factory to port/depots) and secondary dispatch logistics, servicing domestic sales, B2B accounts (RCM), and export channels.

---

## 2. Order Intake & Communication Protocols

### Shared Communication Channels
* **Logistics Order Group:** A centralized messaging channel (WhatsApp) containing sales executives, business development managers, regional managers, and production coordinators.
* **Order Trigger:** Sales representatives post new orders directly into the group, triggering the logistics fulfillment process.

### Minimum Required Order Information

```
                       [Order Intake Post]
                                |
         +----------------------+----------------------+
         |                                             |
[Production Parameters]                       [Logistics Parameters]
  - Product Grade (A/B/C)                      - Destination Address (State/Pin)
  - Packaging SKU (1kg/5kg/bulk)               - Target Delivery Timeline
  - Total Order Volume (MT/kg)                 - Customer Status (New vs. Repeat)
                                               - On-Ground Contact Info
```

* **Data Entry Gaps:** Order requests frequently arrive with incomplete specifications, requiring manual follow-up calls or emails to verify delivery addresses, client tax codes, or packaging preferences.
* **Repeat-Customer Data:** The order intake process does not automatically fetch historical shipping addresses or previous dispatch records, requiring manual record lookup.

---

## 3. Domestic Dispatch Workflow
1. **Validation:** BD/Sales post order info. Logistics validates specifications and requests missing details.
2. **Scheduling:** Logistics coordinates carrier routing. Cut-off thresholds determine same-day or next-day dispatch.
3. **Billing Trigger:** Billing instructions are shared with Accounts to generate the invoice.
4. **Documentation:** Logistics prints three mandatory documents:
   * Commercial Invoice
   * Government E-way Bill
   * Delivery Note
5. **Loading & Dispatch:** Surajmal Khatik supervises vehicle loading, logs the Gate Pass, and updates the tracking spreadsheet.
6. **Transit Status updates:** Shipment progress is shared manually with transporters and sales representatives via dedicated WhatsApp groups.

---

## 4. International Shipping & Export Workflow

### Vessel Booking & Cutoff Management
* **Vessel Scheduling:** Logistics bookings are placed with shipping agents based on target cargo ready dates and carrier schedule listings.
* **Logistics Buffers:** Logistics schedules container stuffing and customs clearances **2–4 days** ahead of vessel cargo cut-off windows to absorb delays in container handovers.
* **20ft Container Prep:** Preparing a 20-foot container for export (including factory-to-port transit and customs document preparation) requires a minimum of **1 week** (stated directly).

### Export Documentation Sequence
1. **Invoice & Declarations:** Accounts generates export invoices based on PO specifications.
2. **Port Delivery & Loading:** Cargo is transported to the Indian departure port and stuffed into containers under customs inspection.
3. **Bill of Lading (BL) Draft:** Logistics reviews the draft BL from the shipping agent, verifies parameters with the customer, and approves issuance.
4. **Agent Handoff:** Shipping documents are shared with port clearance agents at the destination country (e.g., Japan) to coordinate customs clearance.

---

## 5. Time Allocation & Workload Distribution
* **Small Domestic Shipments:** **10%** of Logistics Manager's effort (stated directly) is spent on client and carrier coordination.
* **Large Domestic/B2B Orders:** **30%** of Logistics Manager's effort (stated directly) is spent on routing and scheduling.
* **Communication calls:** Call duration averages **10–15 minutes** for standard dispatches and **20–25 minutes** for complex domestic orders (stated directly).
* **International Dispatch Days:** Consumes **100% (full day)** of the Logistics Manager's effort (stated directly), coordinating physical loading, customs clearance, and freight forwarder routing.
* **Task Delegation:** Data entry, dispatch logging, and tracking updates are managed by the Logistics Executive. The Logistics Manager reviews loading manifests and handles exceptions.

---

## 6. Tooling & Information Systems Context
* **System Integration:**
  * Zoho Books and the tracking spreadsheets operate as separate, disconnected databases.
  * System development preferences prioritize integrating custom tools into existing workflows (Sheets, WhatsApp, email) to minimize tool adoption friction.
  * ERP systems (e.g., SAP) were evaluated and rejected due to cost and implementation complexity (stated directly).
* *Refer to the Tool Stack in the snapshot at the top of this report for system listings.*

---

## 7. Cross-Department Dependencies

| Department | Nature of Dependency | Frequency / Impact |
|---|---|---|
| **Production** | Verifying manufacturing completion dates and stock availability. | Daily / Critical for scheduling |
| **Accounts** | Invoice generation and advance payment verification. | Per-shipment / Transactional |
| **Sales / BD** | Clarifying incomplete order parameters. | Daily / High frequency |
| **Design** | final B2B packaging files for custom pouches. | Per-order onboarding |

---

## 8. Operational Friction & Bottlenecks (Audit Analysis)
*Documented under the Red Flags section at the top of this report.*

---

## 9. Audit Backlog & Follow-Up Items
* **Logistics Data Sync Options:** Research mechanisms to auto-populate shipping fields from Zoho Books invoices directly into the manual tracking spreadsheet.
* **Order Intake Form Integration:** Define mandatory data entry fields for sales teams to reduce incomplete order posts.
* **Carrier Schedule API:** Evaluate shipping carrier APIs to automate vessel schedule checks and alert the BD team of ocean freight delays.
