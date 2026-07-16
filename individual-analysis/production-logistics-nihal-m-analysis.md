# Operational Documentation: Production & Logistics
**Interviewee:** Nihal M Paliwal — Logistics Head, EF Polymer
**Interview Date:** May 29

---

## Department Snapshot

### Time & Effort Split (stated directly by Nihal)
* **Carrier Coordination & Scheduling:** ~35%
* **Documentation & Billing (Invoice/E-Way Bill/BL):** ~30%
* **Exception Chasing, Follow-ups & Data Validation:** ~20%
* **Physical Loading & Stuffing Supervision:** ~15%

> **Manager Comms Overhead (stated directly):**
> * Small/straightforward domestic orders → **10%** of Logistics Manager time on sales coordination
> * Large/complex domestic orders → **30%** of Logistics Manager time
> * International export dispatch day → **100% full day** (stuffing, documentation, freight forwarder mails, follow-ups)

### Tool Stack
* **Order Communication:** WhatsApp (primary, 70-80% of daily comms), Email & Slack (international/official)
* **Tracking & Operations:** Google Sheets (logistics tracking, vendor/partner list, pricing, transit timelines)
* **Invoicing:** Zoho Books (invoice generation and delivery challans — operated by Accounts team)
* **Document Repository:** Google Drive (dedicated folders per client/delivery partner for export docs, PDFs)
* **Physical Records:** Printed files maintained for government audit compliance (Gate passes, challans, transport receipts)

### Key Frequency & Volume Metrics (stated directly)
* **Export Orders:** 10–15 orders per month (~500–600 kg total volume)
* **Domestic Orders:** Handled daily; 70-80% arrive last-minute from Sales
* **Custom Packaging Lead Time:** 15–20 days for printed custom pouches
* **Communication Call Duration (Domestic):** 10–15 minutes per standard order; 20–25 minutes per large/complex order
* **Manual Production Turnaround (e.g., 2 MT batch):** ~10 days
* **Export Container Prep (20ft):** Minimum **1 week** from cargo-ready date to port-ready
* **Vessel Cutoff Buffer:** **2–4 days** ahead of cut-off for container stuffing and customs preparation
* **Logistics Team Scale:** Nihal (Head) + 2 internal team members

### Red Flags
1. **High** — *Last-Minute Orders* — 70–80% of sales orders come at the last moment, causing dispatch rush and documentation errors.
2. **High** — *Incomplete Order Information* — WhatsApp-based order intake regularly has missing fields (pin code, GST number, packaging SKU), requiring back-and-forth clarification before billing can start.
3. **High** — *Custom Packaging Delays* — White-label packaging requires 15–20 days with vendor MOQ constraints; without a sales forecast, this delays dispatch by weeks.
4. **Medium** — *Disconnected Systems* — Zoho Books, Google Sheets, and Google Drive are entirely separate. No single dashboard exists; all data is manually duplicated across systems.
5. **Medium** — *Vessel Schedule Uncertainty* — Vessel prepone/postpone decisions are unpredictable; cargo can miss the vessel cut-off if the prepone notification arrives late.

---

## 1. Operational Profile & Scope
* **Department/Business Unit:** Production & Logistics — manages domestic and international product dispatches, freight booking, customs documentation, inventory coordination, and custom packaging pipeline.
* **Team Structure & Roles:**
  * **Logistics Head (Nihal M Paliwal):** Leads carrier negotiations, plans international vessel bookings, coordinates customs clearance, manages vendor payments, and reports directly to CXOs.
  * **Logistics Team (2 Members):** Handle daily dispatch tracking, data entry into Sheets, courier portal lookups, and domestic order logging.
* **Scope of Activity:**
  * **Domestic:** Coordinates courier/transport partners for domestic B2B orders (RCM, direct sales, BD-initiated).
  * **International/Export:** Manages vessel booking, container stuffing, customs documentation (Invoice, E-Way Bill, BL), and agent coordination at destination ports (e.g., Japan).
  * **Packaging Coordination:** Works with internal Design team and external vendors for custom B2B packaging.

---

## 2. Order Intake & Communication Protocols

### Communication Channels by Use Case

| Channel | Use Case | Frequency |
|---|---|---|
| **WhatsApp** | Domestic order intake, carrier coordination, internal tracking updates | Daily, primary |
| **Email** | International shipments, formal vendor and customer communication | Per shipment |
| **Slack** | Official internal comms for international orders | Per shipment |
| **Google Sheets** | Dispatch status, vendor rates, transit timelines | Continuously updated |

### Order Groups (WhatsApp)
* **Logistics Group:** Contains Sales Executives, BD Managers, RSMs, FSMs, and Production Coordinators. All order intimations land here first.
* **Transporter Groups:** Dedicated per carrier partner; used to share dispatch instructions, tracking numbers, and delivery updates.

### Minimum Required Order Information for Dispatch

**For Billing (Accounts):**
- GST Number
- Billing Party Name & Company Name
- Price (whether inclusive or exclusive of GST)
- Delivery Address (State, Pin Code)

**For Production:**
- Product Grade (e.g., granule size: 1mm–2mm vs. 2mm–4mm)
- Packaging SKU (1 kg, 5 kg, bulk)
- Total Quantity (MT / kg)
- Standard vs. white-label packaging required

**For Logistics:**
- Shipping address & on-ground contact number
- Customer type (New vs. Repeat)
- Urgency / target delivery date

> **Data Gap:** Orders frequently arrive via WhatsApp without the full required fields. Logistics must manually call or message back to get missing information before invoicing and dispatch can begin.

> **Repeat Customer Gap:** For repeat customers, shipping details are NOT auto-fetched; Nihal manually searches previous records or asks the salesperson to reconfirm — a clear candidate for automation.

---

## 3. Domestic Dispatch Workflow

```
Sales/BD posts order on WhatsApp Logistics Group
        ↓
Logistics validates info; requests any missing details
        ↓
Checks freight budget/rate with Sales (standard vs. urgency)
        ↓
Accounts generates Invoice in Zoho Books
        ↓
Logistics selects transport partner (from vendor rate Google Sheet)
        ↓
E-Way Bill + Delivery Note/Challan generated
        ↓
Vehicle arranged; physical loading at factory supervised
        ↓
Gate Pass logged; physical records filed for audit
        ↓
Tracking ID manually fetched from courier portal
        ↓
Tracking status shared back on WhatsApp group + Transporter group
        ↓
Delivery confirmation logged on Google Sheet
```

**Key operational notes:**
- Vendor payments: Nihal receives the vendor invoice and routes it to Accounts for processing.
- **Strategic dispatch timing:** Friday/Saturday dispatches are timed so cargo reaches Mundra port by Monday, maximising the full week for port processing.
- For urgent domestic orders: same-day or next-day dispatch is possible if all order information arrives complete and in time.

---

## 4. International Shipping & Export Workflow

### Volume & Communication
* **Volume:** 10–15 export orders per month
* **Primary Communication Channel:** Email and Slack (for formal audit trail)
* **Drive Folders:** Dedicated Google Drive folder per delivery partner/client; all export documents stored here

### Step-by-Step Export Workflow

```
1. Sales/BD confirms international PO
         ↓
2. Logistics checks vessel schedule → identifies target vessel & cut-off date
         ↓
3. Container booking placed with shipping agent (2–4 day buffer before cut-off)
         ↓
4. Production notified to prepare batch (~10 days per 2 MT)
         ↓
5. Accounts generates export invoice (Zoho Books → PDF → saved to Drive folder → sent via Email)
         ↓
6. Transport arranged: Factory (Jaipur) → Mundra Port
         ↓
7. Container stuffing at port (loading supervised; photos taken as proof of condition)
         ↓
8. Customs queries resolved; shipping line finalizes container entry
         ↓
9. BL (Bill of Lading) draft received from shipping agent → Nihal reviews & approves issuance
         ↓
10. Final documents (Invoice, BL, E-Way Bill) saved to Drive → shared with Sales, Accounts, CXOs
         ↓
11. Documents handed off to destination country clearance agent (e.g., Japan) for customs
         ↓
12. Post-delivery: confirmation from customer/agent → order closed on Sheet
```

### Vessel Schedule Risk (stated directly)
* Vessel prepone/postpone is **unpredictable** — notification typically arrives only once confirmed, often with very little lead time.
* If cargo is not at the port before the cut-off (even by 1–2 days), the vessel is missed entirely.
* Nihal builds a **2–4 day buffer** and uses **Friday/Saturday factory dispatches** to ensure Monday arrival at Mundra, preserving the full next week.
* When a vessel IS missed, the team explores weekend transit options to catch the next available slot.

### Export Container Standards
* **20ft Container:** ~1 week from factory cargo-ready to port-ready (stated directly)
* **40ft Container:** Additional palletisation time; proportionally longer
* **Fixed Route:** Jaipur → Mundra Port (standard; no route renegotiation each shipment)
* **Shipping Line Charges:** ~90% are fixed per route. Additional charges can apply for customs officer fees, documentation errors, war surcharges, or port-specific surcharges — all cited as real-world friction

---

## 5. Custom Packaging & Design Workflow

### Why This Is Complex
* EF Polymer products come in multiple grades with granule size variations (e.g., 1mm–2mm vs. 2mm–4mm). Some customers require specific blends, affecting packaging labeling.
* Many B2B/export clients require **white-label custom packaging** with their own branding, certification marks, and regulatory labeling.

### Packaging Process Flow

```
Sales confirms custom packaging requirement
        ↓
Internal Design team creates packaging artwork
        ↓
Client reviews and approves artwork
        ↓
Certification/regulatory markings added (if applicable)
        ↓
Design sent to external printing vendor
        ↓
Vendor prints (MOQ applies; if order < MOQ, batched with another order)
        ↓
Lead time: 15–20 days standard (urgent prints cost significantly more)
        ↓
Printed pouches arrive at factory for use in packing
        ↓
Production packs material → ready for dispatch
```

> **Key Bottleneck:** If Sales does not share a pipeline forecast in advance, Logistics cannot pre-order pouches. A single packaging delay of 15–20 days can push an entire export shipment to miss its vessel window.

---

## 6. Time Allocation & Workload Distribution

| Scenario | Logistics Head Time Spent | Notes |
|---|---|---|
| Small domestic order (straightforward) | **10%** of day on comms | Complete info arrives; Logistics confirms and delegates to team |
| Large/complex domestic order | **30%** of day on comms + routing | Multiple back-and-forths with Sales, Production, Accounts |
| International dispatch day | **100% of full day** | Stuffing supervision, customs, freight forwarder emails, follow-ups |
| Standard comms call (domestic) | **10–15 minutes** per call | Routine status/clarification |
| Complex comms call | **20–25 minutes** per call | Large domestic or multi-SKU orders |

---

## 7. Cross-Department Dependencies

| Department | Nature of Dependency | Frequency / Impact |
|---|---|---|
| **Sales / BD** | Order initiation, customer details, pricing approval, pipeline visibility for packaging pre-planning | Daily / Critical — most friction originates here |
| **Production** | Batch readiness dates, grade availability, packaging inventory status | Daily / Critical for scheduling |
| **Accounts** | Invoice generation, E-Way Bill, payment confirmation, vendor payment routing | Per-shipment / Transactional |
| **Design** | Custom pouch artwork creation and client approval coordination | Per new B2B/export onboarding |
| **CXOs** | Escalation approvals for high-value shipments; visibility on overall shipment status | As needed / Reporting |

---

## 8. Tooling & Information Systems Context

### Current Tool Stack (As-Is)

| Tool | Owner | Purpose | Pain Point |
|---|---|---|---|
| Google Sheets | Logistics Team | Dispatch tracking, vendor rates, transit timelines, partner contacts | Fully manual; no automation or alerts |
| Zoho Books | Accounts Team | Invoice and challan generation | No integration with Sheets or Drive |
| Google Drive | Shared | Export document repository (per-client folders) | Manual PDF export + upload every time |
| WhatsApp | All | Primary comms and order intake | Unstructured; information frequently incomplete or lost |
| Email | Logistics Head | International formal comms | Disconnected from Sheets/Zoho |
| Slack | Logistics Head | Official internal comms for exports | Disconnected from all other tools |
| Physical Files | Logistics Team | Audit records (Gate passes, challans, transport receipts) | Fully manual; no digital backup |

### SAP Evaluation — Explicitly Rejected
* SAP was evaluated as a potential ERP to unify operations.
* **Decision: Rejected** — Too expensive and too complex to implement for the current team size and workflow maturity (stated directly).

### Tool Adoption Philosophy (stated directly by Nihal)
> *"Our vision is that you don't change our existing workflow. We are making Google Sheets, we are using WhatsApp, emails, Slack — just integrate and improve what we have."*

* Any new tool must work **within or alongside** existing WhatsApp / Google Sheets / Email / Slack workflows.
* Vendors and external partners will **not** adopt a new platform — integrations must keep their experience unchanged.
* Preference: integrate intelligence into existing channels rather than introduce a new standalone system.

---

## 9. Desired Solutions & Future Scope
Requirements stated directly by Logistics Head:

1. **Centralized Shipment Dashboard:** A single source of truth for all domestic and international shipments — replacing scattered Sheets and WhatsApp updates. CXOs (Puran Sir, Narayan Sir) should be able to check any shipment's status without asking Nihal.
2. **Predictive Cost & Time Model:** Based on historical order data, instantly estimate delivery time and transportation cost for a new order so Sales can give accurate commitments to customers without waiting for Logistics to manually calculate.
3. **Exception & Anomaly Alerts:** Flag potential extra charges or delays (e.g., specific-country customs surcharges, vessel prepone risk, packaging inventory not ready) **before** they cause problems.
4. **Automated Documentation Flow:** Eliminate the manual Zoho Books → PDF → Google Drive workflow. Invoices, delivery notes, and export docs should auto-save and be accessible to all stakeholders in one place.
5. **Integration, Not Replacement:** Any new system must integrate into existing workflows (WhatsApp, Google Sheets, Email, Slack) — not replace them.

---

## 10. Audit Backlog & Follow-Up Items
* **Order Intake Standardisation:** Define a mandatory field checklist for Sales when posting orders to the WhatsApp logistics group to eliminate missing-information delays.
* **Packaging Pipeline Visibility:** Create a shared packaging inventory/forecast tracker so Logistics can pre-order custom pouches based on the Sales pipeline.
* **Logistics-Accounts Data Sync:** Research integration to auto-populate dispatch data from Zoho Books into the Google Sheets tracking system, eliminating manual double-entry.
* **Vessel Schedule Monitoring:** Evaluate shipping carrier APIs or agent-provided feeds to get earlier warnings on vessel prepone/postpone events.
* **Vendor Rate Sheet Automation:** Automate rate comparison from the maintained vendor rate sheet when a new order arrives, surfacing the optimal carrier automatically.
