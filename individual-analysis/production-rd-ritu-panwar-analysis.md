# Operational Documentation: Research & Development (R&D)
**Department Lead:** Ritu Panwar — Product Development Manager
**Last Updated:** July 2026 · Based on direct transcript audit (01-rnd.md) + Workflow gap analysis

---

## Department Snapshot

### Time & Effort Split (Revised)
| Activity | % of Team Time | Est. Daily Hours |
|---|---|---|
| Technical, Agronomical & Compliance Documentation | ~30% | ~2.4 hrs |
| Project Tracker Maintenance (Google Sheets) | ~20% | ~1.6 hrs |
| Grant & B2B Proposal Drafting | ~20% | ~1.6 hrs |
| New Product Acquisition & Partner Evaluation | ~15% | ~1.2 hrs |
| Protocol Auditing & Approvals | ~10% | ~48 min |
| Board & BOD Reporting Prep | ~5% | ~24 min |

### Tool Stack (Corrected from Transcript)
| Tool | Usage |
|---|---|
| Google Sheets | 8–10 simultaneous project trackers (India, Japan, EU, USA, registration, QC oversight, internal trials, product acquisition) |
| Google Docs | Scientific white papers, technical reports, registration docs, compliance documentation |
| Google Slides | Presentations for B2B pitching, technical training, partner briefings |
| Paper AI | Online scientific paper referencing — back-linking for scientific documentation and proposals |
| Google Drive | Central file upload, folder management, and cross-team sharing |
| Power BI | Active onboarding by Shubham — GIS dashboards and centralized R&D data reporting |

> **Removed from tool stack:** Wisebase (not mentioned in transcript). Asana was tried but abandoned due to overhead.

### Key Volume Metrics (Direct from Transcript)
- **Active Projects:** 5–6 steady state, **18–20** in peak season
- **Trackers Managed:** ~8–10 independent Google Sheets (Ritu confirmed directly)
- **Protocol Approval Stages:** 3-step (agronomic area fit → objective alignment → budget check)
- **Proposal Drafts per Proposal:** Minimum 2–3 rounds; domestic within 1 week, international 15–20 days
- **Quarterly Proposals:** ~5–6 in steady state; up to 20+ in peak quarters
- **Query SLAs:** General ~1–2 hrs; unexplored topics 3–4 hrs; QC-level 28–30 hrs; field trial 2–3 months

---

## 1. Operational Profile & Scope

- **Department:** R&D / Technical — new product development, crop validation trials, regulatory registration, international technical documentation
- **Geographical Scope:**
  - **India (National):** Direct on-ground trial management, university partnerships, domestic B2B validation, agronomical documentation (primary documentation burden on Ritu)
  - **Europe:** Technical support, protocol design, data oversight. Three local people maintain trackers, but Ritu is the single consolidation point currently. Future agronomist planned.
  - **USA:** Ritu leads agronomist coordination; regional POC manages trackers
  - **Japan:** Same model as USA — regional POC, Ritu leads

---

## 2. Full Team Structure & Responsibilities

| Name | Role | Responsibilities | Reports To |
|---|---|---|---|
| **Ritu Panwar** | Product Development Manager / R&D Lead | New product acquisition, compliance, international protocols (EU/USA/Japan), grant drafting, all international proposals, agronomical documentation (national), protocol approvals (non-delegable final sign-off) | CXO / BOD |
| **Arman** | Product Development Executive | Pilot projects, B2B partnerships, technical training, commercial bridge between R&D and Sales, GIS and data analytics oversight | Ritu |
| **Gaurav (Dr. Gaurav Ayodhya Singh)** | Product Development Executive | Scientific partnerships, internal agronomy, internal & external field validation, crop trial management | Ritu |
| **Swadeep** | Support — Pot Trials | Pot trials and field validation support | Gaurav |
| **Shubham Tetarwal** | Research Executive | Data analytics, GIS (Google Earth Engine / Power BI), market research, dashboard development | Ritu |
| **Manan** | Manager (Joining) | Urban gardening, forestry, government segments | Ritu |
| **Kamlesh Ji** | Formulation Manager (Joining) | R&D formulation, raw material development | Ritu |
| **Field Interns** | Project Basis (6-month rotations) | Field trials, POCs, farmer engagement — UP, Gujarat, Rajasthan and other regions | Arman |

---

## 3. Proposal Development & B2B Pipeline

### Ownership Split
- **B2B Proposals:** Arman (domestic partners, on-ground pilots)
- **Scientific University Proposals:** Gaurav
- **International Proposals & Grant/Subsidiary Proposals:** Ritu (non-delegable)

### Proposal Volume & Cycle
- Steady state: 5–6 proposals/quarter
- Peak: 20+ proposals (minor + major combined)
- Average minimum 2–3 drafts per proposal before acceptance
- Novel use-cases (saline conditions, hydroponics, tissue culture, N2O studies) require entirely custom proposals — no template reuse possible

### Key Challenge
No shared proposal template library. Each proposal is built from scratch. No standardised intake format from Sales/BD, so requests arrive with incomplete context, adding back-and-forth rounds.

---

## 4. Trial Lifecycle & Cost Exposure

### Full Flow (Production → QC → R&D → Trial → Outcome)
```
[1] Formulation Ready
    ↓
[2] Assign Lot Number (Production)
    ↓
[3] QC Test (Production runs 24-hr batch quality test)
    ↓
[4] QC Report issued → R&D logs result, links to trial tracker on Google Drive
    ↓                    ⚠ Break here = data lost or misfiled
[5] Design Regional Protocols (Ritu — non-delegable 3-step approval gate)
    ↓
[6] Deploy Trial (2–4 months in field)
    ↓
    ├── [Success] → Final Report filed to R&D Drive
    └── [Failure / Data Loss] → Re-run Trial (ADDS DIRECT COST)
```

### 3-Department Handoff Detail (Step 2–4)
| Step | Owner | Action | Risk if skipped |
|---|---|---|---|
| Lot Assignment | Production | Assigns lot number, ships sample | Wrong lot = invalid trial data |
| QC Test (24 hrs) | Production / QC | Full batch quality run | Skipping means trial with bad product |
| QC Report | QC | Issues report for the lot | No report = no basis for trial sign-off |
| Data Logging | R&D (Ritu / team) | Links lot to tracker + files to Drive | Not done = data silo, future data loss |

- **Largest Cost Center:** Validation and trials
- **Primary Risk:** Without a unified database of past trial outcomes, the team cannot verify if a similar test was already run — leading to preventable repeat experiments
- **Ritu's Direct Quote:** *"If a monitoring system existed where field data was automatically submitted, we wouldn't overspend on the collection part."*
- **No Live Dashboard:** Zero real-time visibility of cost committed vs. spend to date per trial/project

---

## 4b. Documented Workflows (All 6 — from Audit)

### Workflow 1 — Product Validation & Trial Lifecycle
See Section 4 above for the full flow. Key friction: the Production→QC→R&D chain is a 3-party handoff with no automated trigger — a missed step means the lot data is never linked to the trial tracker.

---

### Workflow 2 — B2B Proposal & Protocol Drafting
**Trigger:** BD or Sales brings a new use case or partner lead.

```
Intake Novel Use Case
    ↓
Case-by-case Scientific Research (Gaurav for scientific; Ritu for international)
    ↓
PD Manager Drafts B2B / Grant Proposal  ← ⚠ Bottleneck
    ↓
3-Step Protocol Auditing (see Workflow 3)
    ↓
Multi-Round Review (Domestic: ~1 week | International: 15–20 days, min 3 drafts)
```

**Ownership by proposal type:**
| Proposal Type | Owner | SLA |
|---|---|---|
| B2B (domestic partners, pilots) | Arman | ~1 week |
| Scientific / University | Gaurav | ~1 week |
| International / Grant / Subsidiary | Ritu (non-delegable) | 15–20 days, 3+ drafts |

**Volume:** 5–6/quarter steady state; up to 20+ in peak quarters

---

### Workflow 3 — Protocol Approval Gate *(Non-Delegable)*
**Trigger:** Any trial request from BD, Sales, or university partners.

```
Trial Request Received (from BD / Sales / University)
    ↓
STEP 1 — Agronomical Area Fit
         Study farming style, crop type, regional conditions
         → Is EFP product compatible with this area?
    ↓
STEP 2 — Objective Alignment
         Does the product meet the trial's stated objectives?
    ↓
STEP 3 — Budget Check
         Is the trial within the approved budget envelope?
    ↓
    ├── [Pass] → Ritu signs, marks approval, dispatches to team
    └── [Fail at any step] → Feedback sent to requester
```

**Critical constraint:** All 3 steps are personally executed by Ritu Panwar. This gate applies to **every** trial — not just B2B proposals. With 18–20 active projects in peak season, compounded approval load is entirely centralised on one person.

---

### Workflow 4 — Multi-Tracker Data Flow & Consolidation
**Current architecture:** 8–10 independent Google Sheets feeding into Ritu as the sole consolidation point.

| Tracker | Data Source | Ritu's Role | Consolidation Risk |
|---|---|---|---|
| India Tracker | Gaurav manages inputs | Leads & reviews | Low — internal |
| EU Tracker | 3 local staff maintain separately | Consolidates into single file | **High** — 3 sources, manual merge |
| USA Tracker | Regional POC inputs | Leads remotely | Medium — timezone gap |
| Japan Tracker | Regional POC inputs | Leads remotely | Medium — timezone gap |
| QC Tracker | Production updates daily | Oversees & reviews | Medium — cross-dept dependency |
| Sample / Lot Tracker | Production lot numbers | Logs & links to trial tracker | High — break = data loss |
| Registration Tracker | Ritu | Manages directly | Low |
| Project / Deadline Tracker | Ritu | Manages directly | Low |
| New Product Acquisition | Ritu | Manages directly | Low |
| PPT / Presentation Tracker | Team | Reviews | Low |

**Output of consolidation:** BOD Monthly Report + Project Status updates — both assembled manually by Ritu with no automated aggregation.

**Risk flag:** No cross-referencing between trackers. A trial referenced in the India Tracker has no programmatic link to the sample in the Lot Tracker or the QC report in the QC Tracker.

---

### Workflow 5 — Sales & BD → R&D Query Resolution
**Trigger:** Sales or BD needs technical data to pitch, close, or support a partner.

| Query Tier | Example | Resolution Process | Response Time |
|---|---|---|---|
| **Tier 1 — Known Crop** | Dosage for wheat, crop performance data | Check existing trackers & documentation | **1–2 hours** |
| **Tier 2 — Unexplored Topic** | Saline conditions, hydroponics, tissue culture | Hypothesis-level research + literature synthesis | **3–4 hours+** (may exceed 1 day) |
| **Tier 3 — QC / Absorption Level** | Why is product not absorbing water? | Full QC lab test (24 hrs) + scientific report (~4 hrs) | **28–30 hours minimum** |
| **Tier 4 — Field Trial / POC** | Test product on new crop / plantation type | Arrange field visit + partner + mini-pilot | **2–3 months** |

**Critical gap:** All 4 tiers are routed directly to R&D team members. There is no self-serve knowledge base for Sales or BD. Tiers 3 and 4 have response times measured in days to months — blocking deal closure during that window.

---

### Workflow 6 — Monthly Reporting & BOD Aggregation
**Trigger:** Start of each month — data needed for Board of Directors report.

```
[1] Ritu sends manual reminder emails to all international agronomists
         ⚠ No automated trigger — fully manual
    ↓
[2] Chase follow-ups across time zones (EU · USA · Japan)
         Time zone gap makes synchronisation difficult
    ↓
[3] Collect national & India data from Gaurav, Arman, Shubham
    ↓
[4] Manual aggregation — all sources merged by Ritu into one document
         ⚠ No standard template — format varies each month
    ↓
[5] Compile BOD summary — tag CXOs on high-cost or strategic items
    ↓
[6] Present to CXOs & Board of Directors
         Monthly cycle complete — repeats identically next month
```

**Root cause:** Zero tooling support. No automated reminders, no aggregation template, no pre-built BOD format. Ritu personally coordinates 3+ time zones before she can begin compiling. The process repeats identically every cycle with no improvement.

---

## 5. Tracker Architecture (Full Inventory)

| Tracker | Owner | Purpose |
|---|---|---|
| India Tracker | Gaurav (Ritu leads) | National field trial locations, outcomes, status |
| Japan Tracker | Regional POC (Ritu leads) | Japan trial data, analysis, payment/subsidy |
| EU Tracker | Ritu (3-person local team inputs) | EU trial data — consolidated by Ritu |
| USA Tracker | Regional POC (Ritu leads) | USA trial data, status |
| Internal Trials / Sample Tracker | Ritu / Team | Lot numbers, sample consumption |
| Registration Tracker | Ritu | Step-by-step progress of active regulatory filings |
| QC Tracker | Production (daily) — reviewed by Ritu | Batch quality daily log — crosses into Production dept |
| New Product Acquisition Tracker | Ritu | Products, partners, onboarding pipeline |
| Project / Deadline Tracker | Ritu | Active project timelines, deadlines, BOD deliverables |
| PPT / Presentation Tracker | Team | Slide tracking for major presentations |

---

## 6. Cross-Department Dependencies

| Department | Nature of Dependency | Frequency / Impact |
|---|---|---|
| **Sales & BD** | Requests for technical pitch data, crop dosage guidance, field trial results. All queries hit R&D directly — no self-serve mechanism. | Daily / High frequency |
| **Production** | Transitioning lab-scale formulations to commercial scale; lot number coordination for QC and sample allocation | Project-based |
| **QC** | Shared Daily QC Tracker — R&D oversees, Production updates | Daily |
| **Finance** | International trial budget approvals; national vendor/scientific payments; CXO tagged on high-cost approvals | Per-invoice / Transactional |
| **CXOs / BOD** | Monthly data aggregation + BOD-level reporting on R&D progress, trials, and pipeline — compiled manually by Ritu | Monthly |

---

## 7. Pain Points & Red Flags (Updated — Audit-Grounded)

| ID | Pain Point | Impact | Key Evidence |
|---|---|---|---|
| P-01 | **Severe Key-Person Dependency** — All protocol approvals, grant writing, international sign-offs on Ritu alone | Critical | 3-stage non-delegable approval; 15–20 day international bottleneck |
| P-02 | **Scattered Trial & Project Data** — 8–10 disconnected Google Sheets, no search or cross-referencing | Critical | Redundant testing; data loss; cannot retrieve past trial results |
| P-03 | **No Trial Cost Monitoring** — Largest cost center with no live dashboard | Critical | Repeat trials inflate budget; zero spend visibility per project |
| P-04 | **No Project Management / Workload Tracking** — Asana abandoned; no capacity visibility | Critical | Cannot know if team member is overloaded before assigning; missed deadlines |
| P-05 | **Repetitive Agronomical Documentation** — National-side technical/agronomical reports written fresh each time by Ritu | High | One of Ritu's top two personal time sinks; no template or delegation path |
| P-06 | **Proposal Drafting Fragmentation** — No shared template bank; each proposal built from scratch by different people | High | 5–6 to 20+ proposals/quarter; minimum 2–3 drafts each |
| P-07 | **Broken Information Flow to Sales & BD** — No self-serve knowledge base; all queries route to R&D manually | High | Simple queries: 1–2 hrs; QC-level: 28–30 hrs; field trial: 2–3 months |
| P-08 | **Manual Reporting Reminders & BOD Aggregation** — Ritu manually chases international agronomists; BOD report assembled by hand | Medium | Monthly cross-timezone data collection with no automation |

---

## 8. Recommended Solution Segment

### Implementation Required

**Solution Overview & Key Features:**
- **R&D Frontend Dashboard:** Build a front-end module (Dashboard) for the R&D branch lead to track all key decisions, scattered data (trials, project data, costing, and visibility) in one place.
- **Bi-Directional Sync:** Connect the dashboard directly to all existing Google Sheets. Updating items in sheets automatically reflects on the dashboard, and updates made via the dashboard push directly to the sheets.
- **Approval Flow System:** Integrate an approval flow on the dashboard, where the R&D head can view, request, approve, or reject approvals needed from the team (with requests routing to/from sheets or dashboard directly).
- **Workload & Project Management:** Integrate project management and workload tracking on the dashboard so the R&D head can see team capacity, timelines, and project reversions.
- **Proposal Drafting Engine:** Build a custom proposal drafting engine (using prompts via Gemini/LLMs) that interfaces with a backend RAG agent (Knowledge Base) over existing Google Drive data to draft specific format proposals automatically.
- **Single Source of Truth AI Chatbot:** Upgrade the existing R&D AI chatbot to include the full knowledge base, connected to the dashboard to fix broken information flows to Sales/BD.
- **Automated Reporting Reminders:** Establish automated reporting and reminder workflows via API integrations (WhatsApp for the internal team, Slack for the international team, and Gmail for external partners like US/Europe aggregators).
- **Unified Organization OS:** Ensure this forms part of a single operating system for EF Polymer where CXOs have role-based, one-click visibility.

**What Remains the Same:**
- **No New Backend Database:** Existing Google Sheets and Google Drive remain the backend data sources.
- **Familiar Workflows:** The team does not have to migrate away from using Google Sheets or Google Drive. They can still update sheets manually if they prefer.

**What New is to be Built:**
- A unified Frontend Dashboard for R&D operations.
- Bi-directional sync pipelines between the Dashboard and Google Sheets/Drive.
- Custom Proposal Drafting Engine powered by GenAI (e.g., Gemini).
- Upgraded Knowledge Base AI Chatbot (RAG Agent over Google Drive).
- Automated notification integrations for reminders (WhatsApp, Slack, Gmail).

**Tech Stack to be Utilized:**
- **Frontend:** ReactJS + TypeScript.
- **Backend / Storage APIs:** Google Workspace APIs (Google Sheets API, Google Drive API).
- **AI / LLM:** Gemini (or similar) for the Proposal Drafting Engine and RAG Agent.
- **Communication Integrations:** WhatsApp API, Slack API, Gmail API.
- **Deployment:** Google Cloud Platform (utilizing the existing Google Suite workspace for efficient usage-based pricing).

**Problems Solved:**
- Eliminates manual chasing of data and broken information flows across time zones.
- Resolves the massive documentation and proposal drafting bottleneck (saving significant PD Manager time).
- Centralizes project, trial, and workload tracking without forcing the team onto a new complex PM tool.
- Provides CXOs and department heads instant, single-click visibility into costs, timelines, and team capacity.
- Fixes the fragmented approval process by giving a unified approval flow.

### Future Scope of Improvement / Enhancement
- **AI Operations Agent:** In the future, an AI agent could be added to actively monitor task/trial data, identify bottlenecks, flag delays, and analyze team communications for proactive management. This is not needed right now but is a planned future enhancement.

### Next Steps for Team Adoption
- **Mandatory Training:** Team adoption and training sessions must be made compulsory to ensure all team members understand how to use the dashboard and AI tools.
- **Feedback Loop:** Establish a continuous feedback loop to iterate on the solution on the ground, ensuring it genuinely adapts to the team's operational reality and achieves actual adoption.

---

## 9. Audit Backlog & Follow-Up Items

- **Arman's Workflow Audit:** Schedule a session with Arman to map B2B partnership pipeline, GIS analytics, and technical training workflows in detail
- **Power BI Dashboard Validation:** Review Shubham's Power BI and Google Earth Engine onboarding progress to evaluate replacement potential for manual trackers
- **Formulation Manager Onboarding:** Document the workflow transition once Kamlesh Ji is onboarded — particularly how formulation tracking integrates with existing trackers
- **Manan's Segment Coverage:** Once Manan joins, map urban gardening, forestry, and government segment workflows separately
- **EU Tracker Consolidation:** Confirm the 3-person EU local team data workflow and how Ritu's consolidation step can be automated when the local agronomist joins
