# Solution Design Framework
### For converting enterprise audit findings into adoptable, fixable tech solutions

---

## 1. Core Philosophy

Every audit finding tempts you to build something new. Resist that by default. This framework exists to force three questions before any solution is proposed:

1. **Can this be solved by extending what the ground team already uses, instead of replacing it?**
2. **Can we actually build/ship this ourselves with tech — or does it depend on someone else changing behavior?**
3. **Is the fix proportional to the problem**, or are we over-engineering a visibility gap into a platform migration?
4. **Can this be solved by connecting to existing cross-departmental data/systems?** If another department already maintains a sheet with relevant data, connect to it for visibility rather than building a siloed departmental solution.

If a recommendation fails any of these, it isn't a solution yet — it's a wishlist item.

### Guiding Principles

| Principle | What it means in practice |
|---|---|
| **Adoption over architecture** | A dashboard nobody updates is worse than a spreadsheet everyone does. Meet the ground team where they already work. |
| **Extend, don't replace** | Wrap intelligence (visibility, alerts, analysis) around existing tools via APIs/integrations rather than migrating users to new systems. |
| **Cross-departmental connection over isolation** | If another department already maintains a sheet or system with the data, connect to it to gain visibility. Don't build a siloed solution if cross-departmental analysis solves it. |
| **Fixable-only** | Only recommend what we can build. "Ask the regional team to update the sheet daily" is not a solution — it's a hope. If there's no tech lever, don't include it. |
| **Right tool for the job, not the flashiest tool** | A WhatsApp alert can solve a problem a custom dashboard can't, because that's where the ground team already lives. |
| **Show expertise where it counts** | Default to lightweight integration — but when a genuine custom tool (e.g., an AI drafting assistant) removes real manual effort, build it. Adoption-first doesn't mean low-ambition. |

---

## 2. The Solution Design Process

Apply this sequence to **every individual audit finding**, not to the audit as a whole. Each finding gets its own pass.

**Step 1 — Isolate the actual problem**
Name it precisely: is this a *visibility* gap, an *alerting* gap, a *data entry/update friction* gap, a *manual repetitive task*, or a *cross-tool disconnection*? Vague problems produce vague (and usually over-built) solutions.

**Step 2 — Map the current workflow**
What tool(s) does the ground/tertiary team already use to do this today (Sheets, WhatsApp, email, a legacy tool)? Who owns the data entry? Who needs the visibility but doesn't have it?

**Step 3 — Apply the Extend-vs-Build test**
- If the data already lives somewhere (Sheets, a legacy tool, WhatsApp threads) → **extend/integrate**.
- If there's genuinely no existing system and the task is manual/repetitive with no tool at all → **custom build** is justified.
- If unsure, default to extend. Escalate to build only if extension can't realistically solve it.

**Step 4 — Match the problem to a Solution Pattern** (see Section 3)

**Step 5 — Select the tech stack** from the approved stack (Section 4), adding only what's genuinely necessary beyond it.

**Step 6 — Design for zero/low friction adoption**
The ground team's daily workflow should change as little as possible. The complexity should be absorbed by us (via integration/AI layer), not pushed onto them.

**Step 7 — Run the Fixable Filter** (see Section 5) before finalizing
Strip out anything that depends on a behavior change, policy change, or org decision with no tech lever attached.

---

## 3. Solution Pattern Library

Use this as a lookup table when a problem is identified — most audit findings will map to one of these patterns.

| Problem Type | Pattern | Example |
|---|---|---|
| **Visibility / reporting gap** (owner can't see ground-level data) | Connect a dashboard directly to the existing data source via API — don't migrate data entry | Sheets API pulls into a live dashboard; ground team keeps using Sheets, owner gets visibility + analysis layer on top |
| **Alerting / notification gap** | Push alerts through the channel already in daily use | WhatsApp alerts for threshold breaches, approvals, escalations — instead of a new notifications inbox nobody checks |
| **Data update friction** (data goes stale because updating is inconvenient) | AI layer that ingests unstructured input from the existing channel and updates the system of record | An AI agent reads WhatsApp messages/images and auto-updates the relevant Sheet/system, so field staff never have to "log in" anywhere |
| **Manual, repetitive knowledge work** (drafting, documentation, summarization) | Custom-built AI tool targeted at that specific task | Proposal drafting assistant, audit documentation generator, report summarizer |
| **Cross-tool disconnection** (data trapped in one tool, needed in another) | Connector/integration between the two, rather than forcing consolidation into one platform | Slack ↔ Sheets ↔ CRM sync via API/connector |
| **Decision-support / analysis gap** (data exists but no insight is derived from it) | An AI/analytics layer (Gemini) reading from existing data sources to generate insights, summaries, or flags | Weekly auto-generated insight summary from Sheets data, surfaced via dashboard or WhatsApp digest |

---

## 4. Approved Tech Stack

Default to this stack. Only introduce something outside it if the pattern genuinely requires it — and flag it explicitly as an addition when you do.

| Layer | Tools |
|---|---|
| **Infrastructure** | Google Cloud Platform (primary) |
| **Data source integration** | Google Sheets API, third-party connectors (Slack, CRM, legacy tools, etc.) |
| **Communication / alerting** | WhatsApp Business API |
| **AI / Intelligence layer** | Gemini LLM, LangChain / LangGraph (for agentic workflows, e.g. WhatsApp → system updates) |
| **Application layer (when a custom tool is genuinely needed)** | React + Node.js + TypeScript |
| **Orchestration** | LangGraph for multi-step/agentic flows (e.g., ingest → classify → update → notify) |

---

## 5. The "Fixable" Filter

Before a recommendation goes into the final solution design, run it through this checklist. If it fails any line, cut it or rewrite it as a tech-enabled alternative.

- [ ] Can this be **built and shipped by us** using the approved stack (or a clearly justified addition)?
- [ ] Does it avoid depending on **someone else changing behavior** with no tech mechanism enforcing/enabling it? (e.g., "team should update Sheet daily" → fails, unless paired with an automated reminder/AI ingestion layer that makes it near-effortless)
- [ ] Does it avoid requiring a **policy, org-structure, or staffing change** to work?
- [ ] Is there a **clear technical deliverable** attached (API integration, dashboard, bot, connector, custom tool) — not just a suggestion?

If a real root cause exists but has no fixable angle, note it separately as an **"Out of scope — organizational"** observation rather than folding it into the solution list. Keep the two clearly separated so the solution design section stays 100% actionable.

---

## 6. Solution Design Template

Use this per audit finding to keep output consistent:

```
Finding: [audit finding as stated]
Problem Type: [visibility / alerting / data friction / manual task / disconnection / analysis gap]
Current Tool(s) in Use: [e.g., Google Sheets, WhatsApp, none]
Root Cause: [why the gap exists today]
Approach: [Extend existing tool / Custom build — with justification if build]
Proposed Solution: [specific description]
Tech Stack: [from Section 4, + any justified addition]
Adoption Impact: [what changes for the ground team — aim for "nothing" or "minimal"]
Owner-Side Benefit: [visibility/analysis/control gained]
Complexity: [Low / Medium / High]
```

---

## 7. Anti-Patterns to Avoid

- **New platform for old workflows** — introducing a new system that the ground/tertiary team must adopt when an integration onto their existing tool would work.
- **Behavior-dependent recommendations** — "the team needs to be more disciplined about updating X" with no tech mechanism attached.
- **Over-tooling a small gap** — building a full custom application for a problem a dashboard or alert could solve.
- **Under-tooling a real repetitive-effort problem** — defaulting to "just connect it" when the actual pain is manual drafting/analysis work that a custom AI tool would meaningfully remove.
- **Stack sprawl** — introducing new tools/services outside the approved stack without explicit justification.