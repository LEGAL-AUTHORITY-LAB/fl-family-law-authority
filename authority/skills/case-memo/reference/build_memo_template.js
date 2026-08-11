const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, ExternalHyperlink,
  Header, Footer, PageNumber, LevelFormat, convertInchesToTwip, VerticalAlign
} = require("docx");
const fs = require("fs");

// FMLG Brand colors
const PINK = "FF1F8E";
const ORANGE = "FF6B00";
const LIME = "C8D400";
const TEAL = "00B5B8";
const BLACK = "0D0D0D";
const MIDGRAY = "888888";
const LIGHTGRAY = "DDDDDD";
const PAPERWHITE = "F7F5F0";
const LIGHTPINK = "FFE5F3";

const FONT = "Arial";

// ---- Helpers ----

function colorBar() {
  // four equal-width table cells, no borders, as the brand color bar
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({
        height: { value: 120, rule: "exact" },
        children: [
          new TableCell({ width: { size: 25, type: WidthType.PERCENTAGE }, shading: { fill: PINK, type: ShadingType.CLEAR }, borders: noBorders(), children: [new Paragraph("")] }),
          new TableCell({ width: { size: 25, type: WidthType.PERCENTAGE }, shading: { fill: ORANGE, type: ShadingType.CLEAR }, borders: noBorders(), children: [new Paragraph("")] }),
          new TableCell({ width: { size: 25, type: WidthType.PERCENTAGE }, shading: { fill: LIME, type: ShadingType.CLEAR }, borders: noBorders(), children: [new Paragraph("")] }),
          new TableCell({ width: { size: 25, type: WidthType.PERCENTAGE }, shading: { fill: TEAL, type: ShadingType.CLEAR }, borders: noBorders(), children: [new Paragraph("")] }),
        ],
      }),
    ],
  });
}

function noBorders() {
  return {
    top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
    bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
    left: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
    right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  };
}

function spacer(h = 100) {
  return new Paragraph({ spacing: { after: h }, children: [] });
}

function sectionHeading(text, color = PINK) {
  return new Paragraph({
    spacing: { before: 300, after: 150 },
    border: { bottom: { color: color, space: 4, style: BorderStyle.SINGLE, size: 8 } },
    children: [
      new TextRun({ text: text.toUpperCase(), bold: true, size: 26, color: color, font: FONT }),
    ],
  });
}

function subLabel(text) {
  return new Paragraph({
    spacing: { before: 200, after: 80 },
    children: [
      new TextRun({ text: text.toUpperCase(), bold: true, size: 20, color: TEAL, font: FONT }),
    ],
  });
}

function body(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 120, line: 276 },
    children: [new TextRun({ text, size: 22, font: FONT, ...opts })],
  });
}

function bullet(text, opts = {}) {
  return new Paragraph({
    numbering: { reference: "bullet-list", level: 0 },
    spacing: { after: 80, line: 264 },
    children: [new TextRun({ text, size: 22, font: FONT, ...opts })],
  });
}

function checkboxItem(text) {
  return new Paragraph({
    spacing: { after: 80, line: 264 },
    indent: { left: 360 },
    children: [
      new TextRun({ text: "☐  ", size: 22, font: FONT, bold: true, color: TEAL }),
      new TextRun({ text, size: 22, font: FONT }),
    ],
  });
}

function doneItem(text) {
  return new Paragraph({
    spacing: { after: 80, line: 264 },
    indent: { left: 360 },
    children: [
      new TextRun({ text: "✓  ", size: 22, font: FONT, bold: true, color: TEAL }),
      new TextRun({ text, size: 22, font: FONT }),
    ],
  });
}

function flagBox(titleText, lines) {
  // Pink left border callout box
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({
        children: [
          new TableCell({
            width: { size: 100, type: WidthType.PERCENTAGE },
            shading: { fill: LIGHTPINK, type: ShadingType.CLEAR },
            borders: {
              top: { style: BorderStyle.SINGLE, size: 4, color: LIGHTPINK },
              bottom: { style: BorderStyle.SINGLE, size: 4, color: LIGHTPINK },
              right: { style: BorderStyle.SINGLE, size: 4, color: LIGHTPINK },
              left: { style: BorderStyle.SINGLE, size: 36, color: PINK },
            },
            margins: { top: 150, bottom: 150, left: 200, right: 200 },
            children: [
              new Paragraph({
                spacing: { after: 100 },
                children: [new TextRun({ text: titleText, bold: true, size: 22, color: BLACK, font: FONT })],
              }),
              ...lines.map(l => new Paragraph({
                spacing: { after: 80, line: 264 },
                children: [new TextRun({ text: l, size: 21, font: FONT })],
              })),
            ],
          }),
        ],
      }),
    ],
  });
}

function staffHeaderCell(text, fill) {
  return new TableCell({
    width: { size: 100, type: WidthType.PERCENTAGE },
    shading: { fill: fill, type: ShadingType.CLEAR },
    margins: { top: 100, bottom: 100, left: 150, right: 150 },
    children: [
      new Paragraph({
        children: [new TextRun({ text: text.toUpperCase(), bold: true, size: 24, color: "FFFFFF", font: FONT })],
      }),
    ],
  });
}

function staffBlock(name, colorFill, tasks) {
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({ children: [staffHeaderCell(name, colorFill)] }),
      new TableRow({
        children: [
          new TableCell({
            width: { size: 100, type: WidthType.PERCENTAGE },
            borders: {
              top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
              bottom: { style: BorderStyle.SINGLE, size: 6, color: LIGHTGRAY },
              left: { style: BorderStyle.SINGLE, size: 6, color: LIGHTGRAY },
              right: { style: BorderStyle.SINGLE, size: 6, color: LIGHTGRAY },
            },
            margins: { top: 150, bottom: 150, left: 200, right: 200 },
            children: tasks.map(t => checkboxItem(t)),
          }),
        ],
      }),
    ],
  });
}

function factTable(rows) {
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    columnWidths: [3000, 7000],
    rows: rows.map(([label, value]) => new TableRow({
      children: [
        new TableCell({
          width: { size: 30, type: WidthType.PERCENTAGE },
          shading: { fill: PAPERWHITE, type: ShadingType.CLEAR },
          margins: { top: 100, bottom: 100, left: 150, right: 150 },
          borders: {
            top: { style: BorderStyle.SINGLE, size: 4, color: LIGHTGRAY },
            bottom: { style: BorderStyle.SINGLE, size: 4, color: LIGHTGRAY },
            left: { style: BorderStyle.SINGLE, size: 4, color: LIGHTGRAY },
            right: { style: BorderStyle.SINGLE, size: 4, color: LIGHTGRAY },
          },
          children: [new Paragraph({ children: [new TextRun({ text: label, bold: true, size: 20, font: FONT, color: BLACK })] })],
        }),
        new TableCell({
          width: { size: 70, type: WidthType.PERCENTAGE },
          margins: { top: 100, bottom: 100, left: 150, right: 150 },
          borders: {
            top: { style: BorderStyle.SINGLE, size: 4, color: LIGHTGRAY },
            bottom: { style: BorderStyle.SINGLE, size: 4, color: LIGHTGRAY },
            left: { style: BorderStyle.SINGLE, size: 4, color: LIGHTGRAY },
            right: { style: BorderStyle.SINGLE, size: 4, color: LIGHTGRAY },
          },
          children: [new Paragraph({ children: [new TextRun({ text: value, size: 20, font: FONT })] })],
        }),
      ],
    })),
  });
}

function hyperlinkPara(text, url) {
  return new Paragraph({
    spacing: { after: 150 },
    children: [
      new ExternalHyperlink({
        link: url,
        children: [new TextRun({ text, size: 20, font: FONT, color: TEAL, underline: {} })],
      }),
    ],
  });
}

// ---- Document Assembly ----

const SP_LINK = "https://slgpa2013.sharepoint.com/:f:/r/sites/FAMILYMATTERSLAWGROUPMATTERS/Shared%20Documents/OPEN%20FILES/MATTERS%20-%20OPEN/TORRES,%20NATASHA%20-%20Modification%202026-1330?csf=1&web=1&e=SXSFR3";

const doc = new Document({
  numbering: {
    config: [
      {
        reference: "bullet-list",
        levels: [
          { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 260 } } } },
        ],
      },
    ],
  },
  sections: [
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 720, bottom: 900, left: 900, right: 900 },
        },
      },
      footers: {
        default: new Footer({
          children: [
            new Paragraph({
              border: { top: { color: TEAL, space: 4, style: BorderStyle.SINGLE, size: 6 } },
              tabStops: [{ type: "right", position: 10440 }],
              children: [
                new TextRun({ text: "Family Matters Law Group, P.A.  •  Confidential  •  Torres Intake Summary Memo", size: 16, color: MIDGRAY, font: FONT }),
                new TextRun({ text: "\tPage ", size: 16, color: MIDGRAY, font: FONT }),
                new TextRun({ children: [PageNumber.CURRENT], size: 16, color: MIDGRAY, font: FONT }),
                new TextRun({ text: " of ", size: 16, color: MIDGRAY, font: FONT }),
                new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: MIDGRAY, font: FONT }),
              ],
            }),
          ],
        }),
      },
      children: [
        colorBar(),
        spacer(200),

        new Paragraph({
          alignment: AlignmentType.LEFT,
          children: [new TextRun({ text: "FAMILY MATTERS LAW GROUP, P.A.", bold: true, size: 32, font: FONT, color: BLACK })],
        }),
        new Paragraph({
          spacing: { after: 100 },
          children: [new TextRun({ text: "Internal Attorney-Supervised Work Product — Privileged & Confidential", italics: true, size: 18, font: FONT, color: MIDGRAY })],
        }),

        new Paragraph({
          spacing: { before: 200, after: 200 },
          children: [new TextRun({ text: "TORRES INTAKE SUMMARY MEMO", bold: true, size: 30, font: FONT, color: PINK })],
        }),
        new Paragraph({
          spacing: { after: 300 },
          children: [new TextRun({ text: "Prepared for: Nazarena Hauser, Esq.", bold: true, size: 22, font: FONT, color: BLACK })],
        }),

        factTable([
          ["Re:", "Torres v. Velez — Post-Judgment Modification (Parenting Plan, Timesharing, Parental Responsibility & Child Support)"],
          ["FMLG Matter No.:", "2026-1330"],
          ["Underlying Case No.:", "2020-008873-FC-04, Division FC-29 — Miami-Dade County, 11th Judicial Circuit"],
          ["Filing Venue:", "Broward County — new matter, per Naz's direction"],
          ["Client:", "Natasha Torres — Petitioner"],
          ["Opposing Party:", "Juan Arturo Velez"],
          ["Minor Child:", "Jovanni Velez, DOB 12/18/2013 (age 12)"],
          ["Date:", "07.07.26"],
          ["Purpose:", "Summary of completed intake call, case posture, and flagged issues for attorney review and approval to proceed"],
        ]),

        spacer(150),
        hyperlinkPara("→ SharePoint Matter Folder (source of truth — all documents referenced below)", SP_LINK),

        // WHAT'S BEEN COMPLETED
        sectionHeading("What's Been Completed", PINK),
        body("The intake call with Natasha Torres has been completed. The following work is done and ready for your review:", { bold: true }),

        doneItem("Intake call with Natasha Torres — COMPLETE"),
        doneItem("Retainer signed and executed (06.24.26 via e-signature) — Hourly contract, full representation, $5,000 initial retainer, $450/attorney and $200/paralegal billing rate"),
        doneItem("Full client intake forms completed — UCCJEA affidavit, CS intake questionnaire, financial information"),
        doneItem("Underlying case number confirmed — 2020-008873-FC-04, Division FC-29, Miami-Dade County; new matter to be filed in Broward per Naz's direction"),
        doneItem("Child support modification confirmed in scope — addressed under §61.30 based on changed timesharing; already incorporated into the draft petition"),
        doneItem("Prior order located and reviewed — Agreed Order Adopting Mediated Paternity Agreement and Parenting Plan, entered 10.14.20; child support was set at zero based on equal timesharing"),
        doneItem("Safety Plan received and reviewed — full document analysis completed (see flagged issue below — this document is confusing and needs your direct review)"),
        doneItem("Draft Supplemental Petition for Modification prepared — now at v3, fully populated with case-specific facts (LMW)"),
        doneItem("Draft UCCJEA Affidavit prepared (LMW)"),
        doneItem("SharePoint matter folder set up and accessible (link above)"),

        // CASE POSTURE
        sectionHeading("Case Posture & Key Facts", ORANGE),

        subLabel("Client Profile"),
        body("Natasha Torres, DOB 11/21/1987 — Law Enforcement Officer (Miramar PD), annual salary $87,000. Address: 1456 SW 98th Ln, Davie, FL 33324."),

        subLabel("Opposing Party"),
        body("Juan Arturo Velez — self-employed, income unknown. Address: 859 NW 16th Terrace, Fort Lauderdale, FL 33311. Counsel status: unknown — needs confirmation."),

        subLabel("What Client Is Seeking"),
        bullet("Sole parental responsibility (currently presumed joint)"),
        bullet("Deviation from 50/50 — formalize primary residence with mother"),
        bullet("Father's timesharing on a request/holiday basis only (no fixed weekend schedule) — subject to Flag 2 below on whether supervision is requested"),
        bullet("Child support modification — confirmed in scope, addressed under §61.30 based on changed timesharing; already included in the v3 draft petition"),

        subLabel("Basis for Modification"),
        bullet("Documented history of domestic violence in father's household"),
        bullet("Father's girlfriend (Karolina Mejia) involved in the incident that triggered the 06/19/26 DCF call"),
        bullet("No-contact orders reportedly violated by father"),
        bullet("DCF involvement as of 06/19/26 — investigation into Karolina Mejia's household; Jovanni was among the children involved"),
        bullet("Safety concerns around timesharing exchanges and father's reliability"),
        bullet("Child's established stability — primary residence with mother since 2022"),

        // CRITICAL FLAGS
        sectionHeading("Critical Flagged Issues — Attorney Action Required", PINK),
        body("These are the open items blocking the petition from being finalized:", { bold: true }),

        spacer(80),
        flagBox("FLAG 1 — Incidents Timeline Still Pending From Client", [
          "The petition's substantial-change-of-circumstances section depends on Natasha's detailed account of specific incidents (dates, descriptions, any police/school/medical reports, impact on the child). This is currently a placeholder in the v3 draft.",
          "Needed from you: Once Natasha provides the timeline, review and direct how the facts should be characterized in the pleading (safety concern vs. parenting-time adjustment vs. best-interests issue).",
        ]),
        spacer(150),

        flagBox("FLAG 2 — Is Supervised Timesharing Being Requested?", [
          "The Safety Plan references facilitation of Juan's visits but does not state whether current contact with Jovanni is supervised or unsupervised. The v3 draft assumes a schedule modification but leaves this specific ask blank.",
          "Needed from you: Confirm whether the petition should affirmatively request supervised timesharing, and if so, on what terms.",
        ]),
        spacer(150),

        flagBox("FLAG 3 — Safety Plan Is Confusing and Needs Your Direct Review", [
          "The Safety Plan document itself is poorly drafted and internally confusing — it conflates two separate family units, leaves the danger-threat and termination sections blank, and is only signed by Natasha (not by DCF or Juan).",
          "The no-contact provision does not clearly name Natasha or Juan — it may actually describe Juan and Karolina Mejia's household instead. It is captioned under Karolina Mejia's DCF case (Intake #I-6112546), not the Torres modification matter.",
          "A full document-by-document breakdown is in the Safety Plan Review Memo v2 (SharePoint, Notes folder). Please review that memo directly and confirm: (a) what legal weight this DCF plan carries in the petition — reference/attach it, or treat as background only, and (b) whether the no-contact scope needs clarification from DCF worker Keneisha Simmscameron before the petition is finalized.",
        ]),
        spacer(150),

        flagBox("FLAG 4 — Filing Mechanics Not Yet Confirmed", [
          "A new Civil Cover Sheet and filing fee are required for the Broward filing — flag for whoever is handling e-filing in the Florida Courts E-Portal. A new summons and proper service on Juan (or his attorney, if represented) will also be needed; the certificate of service in the draft is currently a placeholder.",
          "Needed from you: Confirm service method and whether OP has counsel before the petition is finalized for filing.",
        ]),

        // DOCUMENTS READY
        sectionHeading("Documents Ready for Your Review", TEAL),
        bullet("Torres Supplemental Petition for Modification — v3, fully populated, incidents timeline placeholder pending Natasha's input"),
        bullet("Torres UCCJEA Affidavit — draft, ready for review"),
        bullet("Safety Plan Review Memo v2 — full plain-language breakdown of the safety plan (please review directly — see Flag 3 above)"),

        // MISSING INFO
        sectionHeading("Missing Information & Open Questions", ORANGE),
        subLabel("Legal / Case Posture"),
        checkboxItem("Confirm you are the assigned attorney of record for this matter (not yet marked in Smokeball)"),
        checkboxItem("Decide resolution path — contested litigation vs. mediation-first"),
        checkboxItem("Determine if a companion DV injunction action is warranted"),
        checkboxItem("Confirm what legal weight the DCF safety plan carries in the petition (reference/attach vs. background only)"),

        subLabel("Factual — Required to Finalize the Petition"),
        checkboxItem("Incidents timeline from Natasha — dates, descriptions, any police/school/medical reports, impact on the child"),
        checkboxItem("Whether supervised timesharing is being requested, and on what terms"),
        checkboxItem("Clarification from DCF worker Keneisha Simmscameron on the no-contact provision scope (Natasha ↔ Juan, or Juan ↔ Karolina Mejia)"),
        checkboxItem("Whether OP has counsel; if so, contact information for service"),
        checkboxItem("Service method to be used on Juan"),

        subLabel("Billing / Administrative"),
        checkboxItem("Confirm first retainer payment ($2,500 due 06.25.26) was received"),
        checkboxItem("Calendar second payment due 07.25.26"),
        checkboxItem("Confirm matter is active in Smokeball"),

        // STAFF ACTIONS
        sectionHeading("Staff Action Items", PINK),
        body("Organized by staff member — see the copy-paste task list provided separately for Archie/Smokeball entry.", { italics: true, color: MIDGRAY }),
        spacer(100),

        staffBlock("Naz — Attorney Actions (Priority)", PINK, [
          "Confirm assigned attorney of record for this matter in Smokeball",
          "Review the Safety Plan Review Memo v2 directly and confirm what legal weight the DCF plan carries in the petition",
          "Make a preliminary call on resolution path: contested vs. mediation-first",
          "Determine whether a companion DV injunction action is needed",
          "Decide whether supervised timesharing is being requested, and on what terms",
          "Contact DCF worker Keneisha Simmscameron to clarify the no-contact provision scope",
          "Follow up with Natasha for the incidents timeline needed to finalize the petition",
          "Confirm service method and OP counsel status",
          "Review and approve/revise the v3 Supplemental Petition and UCCJEA Affidavit once the above is resolved",
        ]),
        spacer(150),

        staffBlock("Karen — Matter Organization", ORANGE, [
          "Organize loose root-level SharePoint files into the correct named subfolders",
          "Set calendar reminders for retainer payment confirmation and the 07.25.26 second payment",
          "Prepare Civil Cover Sheet and confirm filing fee for the Broward filing; flag for e-filing staff",
          "Prepare intake call prep timeline and case strategy letter for the client",
          "Notify Sara once attorney confirms financial affidavit is needed for the CS component",
        ]),
        spacer(150),

        staffBlock("Sara — Financial Discovery", TEAL, [
          "Child support is confirmed in scope — begin preparing the Financial Affidavit once Karen confirms",
          "Review client financial documents already collected",
          "Run FA cross-check against supporting documents once available",
        ]),

        spacer(300),
        new Paragraph({
          border: { top: { color: LIGHTGRAY, space: 4, style: BorderStyle.SINGLE, size: 6 } },
          spacing: { before: 200 },
          children: [new TextRun({ text: "Not for client distribution. Attorney-supervised work product — subject to attorney review before use in any filing, communication, or strategy decision.", italics: true, size: 16, color: MIDGRAY, font: FONT })],
        }),
      ],
    },
  ],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync("/mnt/user-data/outputs/07_07_26_-_Torres_-_Intake_Summary_Memo_For_Naz.docx", buffer);
  console.log("Done");
});
