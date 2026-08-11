---
name: fmlg-case-memo
description: >
  FMLG branded case memo generator — use this IMMEDIATELY whenever anyone at
  FMLG asks for a "memo," "summary memo," "intake summary," "memo for Naz,"
  "memo for Leisa," "case memo," "update memo," or any request to compile
  notes, drafts, intake calls, safety plan reviews, correspondence, or case
  status into a single document for an attorney to review and approve.
  Triggers on: "put together a memo," "make me a memo," "summarize this for
  [attorney]," "I need something easy to read for Naz/Leisa," "give her a memo
  to review and approve," "compile my notes into a memo," or any request to
  turn intake calls, drafts, emails, or case notes into an attorney-facing
  summary document. ALWAYS produces a fully branded Word doc (colors, tables,
  callout boxes — not plain text) AND a separate copy-paste staff task list
  formatted for Archie to enter into Smokeball. Never produce a plain-text or
  unbranded memo for this firm — always apply full FMLG visual branding.
---

## FMLG Firm-Wide Conventions (apply to every run of this skill)

These six conventions govern all FMLG skills and override any narrower instruction
below that conflicts with them.

1. **Environment-flexible.** Complete the task in the environment you are already in
   — chat, Desktop, or Cowork. If a different environment would be materially better,
   say so in one line and keep working. Never block, never redirect, never hand off
   instead of doing the work.
2. **Identity over lanes.** Staff assignments in this skill are defaults, not gates.
   Anyone may run any skill. **Attorneys self-approve** — if the person running this
   skill is Naz or Leisa, they *are* the approving attorney. Never tell an attorney to
   route their own work to an attorney for approval. Approval gates mean an approving-
   attorney action is recorded, not that the user must go find someone.
3. **Just run it.** Prerequisite stages are soft checks, never hard gates. Pause only
   for a physically necessary input, and ask for that specific item by name — never
   "complete Stage X first."
4. **Read files first.** Search the entire matter file — including misnamed and
   misfoldered documents — before declaring anything missing. If the file is
   disorganized, offer a file-organizer cleanup rather than reporting a gap.
5. **Transcripts preferred, never required.** A typed memo or rough notes always
   suffice as input.
6. **Write to the command center.** Every stage completion, deadline, lifecycle move,
   and attorney flag is written to the matter's command center before the run ends.

---

# FMLG Case Memo Generator

This skill produces attorney-facing case memos summarizing case status, completed
work, flagged issues, and staff action items — always as a fully branded Word
document, always paired with a copy-paste task list for Smokeball entry.

Every time this skill triggers, produce **two deliverables**:
1. A branded `.docx` memo (visual — colors, tables, callout boxes)
2. A plain-text copy-paste task list grouped by staff member, ready to hand to Archie

---

## 1. Before Writing Anything — Verify Against the Real Record

Never write a memo from assumptions, prior memo drafts, or stale project
summaries. A memo is a snapshot of the CURRENT record — treat every fact as
something to check, not something to carry forward from the last document
that mentioned it.

Before drafting, in this order:

- **Search past conversations** (`conversation_search` / `recent_chats`) for
  the matter name and specific sub-topics (e.g., "child support scope," "case
  number," "petition draft"). Drafting work often happens in a different chat
  than the one where the memo is requested — a prior session may have already
  resolved something an older memo or project file still lists as "TBD" or
  "unconfirmed." Treat resolutions found in past chats as current fact unless
  this session contradicts them.
- **Check SharePoint / connected tools** for the matter if available — the
  matter folder is the source of truth, not Claude's memory of an earlier
  summary.
- Read every relevant file in the project (case launch summary, roadmap,
  safety plan reviews, drafts, intake memos, correspondence) using `view`.
- If the user states a fact directly in the current message (e.g., "child
  support is already in the petition"), that's a firsthand correction and
  overrides any stale project file or prior memo — don't re-flag it as open.
- Note what is **completed** vs. **still genuinely open** vs. **flagged for
  attorney review**. An issue only belongs in "flagged" if it's actually
  unresolved as of the most recent information available — don't repeat a
  flag from an older document once the record shows it's been resolved.
- Pull the SharePoint matter folder link if it's referenced anywhere in the
  project instructions or uploaded files — it always goes near the top of the
  memo as a clickable link.
- If a source document (like a safety plan) is confusing, poorly drafted, or
  internally inconsistent, say so plainly and flag it for the attorney's
  direct review — don't paper over ambiguity with a confident-sounding
  summary. Point to whatever underlying review memo has the detailed
  breakdown rather than re-litigating every detail inline.
- Never assign a staff member a task that IS the deliverable currently being
  produced (e.g., don't tell Karen to "create the task list" when the task
  list is the companion document this skill is generating right now).
- If uncertain whether something is still open, say so honestly rather than
  guessing in either direction.

## 2. Required Memo Sections (in order)

1. **Header block** — firm name, doc title, "Prepared for: [Attorney Name]",
   fact table (Re / Case No. / Client / Opposing Party / Minor Child(ren) / Date / Purpose)
2. **SharePoint link** — clickable hyperlink to the matter folder, placed
   immediately after the header block
3. **What's Been Completed** — everything done to date, as checkmarked items.
   Be specific (dates, documents, who drafted what).
4. **Case Posture & Key Facts** — client profile, opposing party, what's being
   requested, basis for the request — pulled from actual intake/case documents
5. **Critical Flagged Issues** — anything requiring attorney judgment before
   the matter can proceed. Use callout boxes (see Section 4 below). Each flag
   states the issue, why it matters, and exactly what's needed from the attorney.
6. **Documents Ready for Review** — list drafts/memos awaiting attorney
   sign-off, with a one-line status on each
7. **Missing Information & Open Questions** — grouped by category (legal
   posture, factual, billing/admin), as checkboxes
8. **Staff Action Items** — grouped by staff member, as checkboxes, inside
   colored header blocks (see Section 4). Reference the separate task list
   deliverable here rather than duplicating exhaustive detail.
9. **Footer** — standard FMLG confidentiality/work-product line

Omit any section with no content rather than forcing empty sections in.

## 3. Voice

Apply `fmlg-brand-kit` voice rules: plain English, direct, short paragraphs,
no corporate throat-clearing, no sugarcoating. This is an internal document for
an attorney — be blunt about what's wrong, unclear, or unresolved. If a
document (like a safety plan) is a mess, say it's a mess.

## 4. Required Visual Branding — Never Skip This

A plain-text or unstyled Word document is not an acceptable output for this
skill. Every memo must include actual visual formatting:

- **Four-color bar** (Pink #FF1F8E / Orange #FF6B00 / Lime #C8D400 / Teal
  #00B5B8) as a full-width table at the very top of the document
- **Section headings** in Pink or Orange, bold, ALL CAPS, with a bottom border
  rule in the section's color
- **Sub-labels** (e.g. "Client Profile") in Teal, bold, ALL CAPS, smaller size
- **Fact table** for the header block — light gray label column, white value
  column, bordered
- **Flag/callout boxes** for critical issues — light pink fill, thick Pink
  left border, bold title line, using a Word table (single cell) styled as a
  callout, NOT a plain paragraph
- **Staff action blocks** — colored header row (Pink for attorney, Orange for
  paralegal/Karen, Teal for Sara/other staff) with a bordered checklist body
  below it
- **Checkboxes** (☐) for open items, **checkmarks** (✓, Teal, bold) for
  completed items — never plain bullets for status items
- **Footer** with the four-color rule and standard FMLG footer text (firm name
  • Confidential • document name, page X of Y)
- Arial throughout; body copy 11pt/size 22 half-points, section headings
  13pt/size 26 half-points per the brand kit type scale

Build this with the `docx` (npm) library — see `/mnt/skills/public/docx/SKILL.md`
for the docx-js gotchas (dual table widths, ShadingType.CLEAR not SOLID, no
literal bullet characters, etc.). Do not attempt this level of styling with a
plain-text `create_file` — it requires a docx-js build script. A working
reference implementation with all of the above components (color bar, fact
table, flag boxes, staff blocks, footer) exists in this skill's
`reference/build_memo_template.js` — copy and adapt it rather than rebuilding
these helpers from scratch each time.

**Always verify visually before presenting**: convert to PDF and render pages
as images per the docx skill's verification steps, and look at the rendered
output before calling `present_files`. If a flag box or table renders badly
(overflow, wrong color, black table shading), fix it before showing the user.

## 5. The Companion Archie Prompt (Always Produce This Too)

Alongside the `.docx` memo, always produce a plain `.txt` file written as a
**direct instruction to Archie**, not a passive summary or data dump. Archie
executes this — every section should read as something to DO in Smokeball,
using imperative verbs (Update, Add, Create, Assign, Log), not as a report
Archie has to interpret before acting.

Structure:

```
ARCHIE — [MATTER NAME] ([MATTER NO.]) — SMOKEBALL UPDATE

Update the Smokeball file for [Matter] as follows:

UPDATE CASE FILE FIELDS:
- [field]: [new/corrected value]
- [field]: [new/corrected value]
(Only include this block if something is actually new or corrected this
session. If nothing changed, omit the block entirely.)

ADD FILE NOTE:
Log a note dated [date] summarizing today's session: [one tight paragraph —
what was reviewed, what was verified/corrected, what was produced].

CREATE THE FOLLOWING TASKS:

Assign to [Attorney Name] (priority):
1. [task]
2. [task]
...

Assign to [Staff Name]:
1. [task]
...

STILL OPEN — DO NOT CLOSE THESE OUT:
- [one-line item]
- [one-line item]
```

Rules:
- Every block is phrased as an instruction ("Update the case number field
  to...", "Log a note...", "Assign to Karen: ...") — never as third-person
  narration ("The case number was corrected to..."). Archie should be able to
  execute each line without translating it into an action first.
- "Update Case File Fields" only includes facts that are new, corrected, or
  newly resolved THIS session (case numbers, venue, scope determinations,
  corrected names/spellings, document version bumps). Don't restate
  long-standing, unchanged file data here — that's not an update.
- "Add File Note" is a single dated paragraph recapping what was done this
  session, written the way a file note should read in Smokeball, not a bullet
  list. Any fact corrected in "Update Case File Fields" should be referenced
  here too so the note explains why the fields changed.
- "Create the Following Tasks" groups strictly by person, priority order first
  (attorney, then whoever's next in the workflow chain). Number tasks
  sequentially within each person's block — each line is one discrete,
  actionable Smokeball task, not a compound sentence with multiple asks. If a
  person's block is blocked/on hold pending another decision, say so as the
  first line ("HOLD — do not begin until X").
- "Still Open" is a short flat list, no elaboration — enough for Archie to
  know what not to mark complete.
- No markdown formatting, no bold, no headers beyond plain caps — this needs
  to paste cleanly into Smokeball's plain-text fields.
- Never assign a task that IS this deliverable (e.g., don't tell Karen to
  "create the task list").

## 6. File Naming & Output

- Memo: `MM_DD_YY_-_[Matter]_-_[Descriptive Name]_-_v[N].docx` matching the
  firm's existing file naming convention (check the project for the pattern
  already in use, e.g. `07_07_26_-_Torres_-_Safety_Plan_Review_Memo_-_v2.docx`)
- Archie prompt (Update Case File Fields + Add File Note + Create Tasks +
  Still Open, all as direct instructions): `[Matter]_Archie_Prompt.txt`
- Save both to `/mnt/user-data/outputs/` and present both together with
  `present_files` in one call.

## 7. Per-Matter Non-Negotiables

- DV/DCF-involved matters: always state in the memo that attorney sign-off is
  required before further drafting or client/OC communication (per firm
  policy), even if this has been said before in prior memos.
- Never invent facts (case numbers, dates, names) not present in the source
  documents or the user's message — flag them as unconfirmed instead.
- If a source document referenced in the memo (safety plan, prior order, etc.)
  is itself confusing or internally inconsistent, do not resolve the ambiguity
  by picking an interpretation — flag it and point to the detailed review memo.

---

## OUTPUT DELIVERY — FIRM STANDARD (v2, SharePoint-native)

All output from this skill is delivered through `fmlg-sp-connector` (Operation 4).

**Destination:** `Notes/` in the SharePoint matter folder
`Last, First - [Matter Type] (####-####)`. There is no `CLAUDE OUTPUT` folder and
no Dropbox path. (`GAL Notes/` on GAL matters.)

**Filename:** `MM.DD.YY - LastName - DocTitle - v1.ext` — versioned, never overwritten.

**Delivery depends on where this skill is running:**

- **Claude.ai (chat / Projects)** — Claude cannot write to SharePoint. Present the file
  as a **download** and print the destination block: matter folder → `Notes/`, filename,
  version. Never write "saved to SharePoint."
- **Cowork (desktop)** — write to the folder designated for the session (ask once at
  first delivery, reuse thereafter), confirm the **actual path written**, and state
  where the file belongs in SharePoint.

Nothing is filed or sent without attorney sign-off. Time is tracked in Smokeball,
including Claude-assisted work.

