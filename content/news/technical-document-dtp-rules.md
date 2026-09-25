---
title: "Manuals, Datasheets, Catalogs: DTP Rules by Document Type"
date: 2027-02-16T16:13:00+08:00
publishDate: 2027-02-16T16:13:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["DTP", "technical documentation", "manuals", "datasheets"]
keywords: ["technical document dtp", "manual datasheet catalog layout", "multilingual technical documents"]
cover: "/images/news/technical-document-dtp-rules.jpg"
author: "MediaLocalize Team"
summary: "A datasheet is read for 40 seconds at a trade show; a manual is cursed at for three hours on a factory floor. Different documents fail in different ways when translated — the DTP rules that matter, by document type."
---

Ask a DTP operator to typeset "the German version" and the first question back should be: German version of *what*? A one-page datasheet, a 200-page installation manual, and a 400-SKU catalog are three different disciplines wearing the same "technical document" costume. They differ in how readers use them, where translated text breaks them, and what QA has to catch. Treating them identically is how you get datasheets with orphaned spec rows, manuals with warnings reflowed onto the wrong page, and catalogs whose German part descriptions push prices off the grid. Here are the working rules, by type.

## Datasheets: density is the design

Datasheets are glance documents — a buyer scans specs for under a minute, often printed at a trade show booth. Everything serves the table:

- **The spec table is sacred.** Row order, units, and column alignment must survive translation untouched. Translate row labels, never values — and keep numbers and units formatted per target-market convention (decimal commas for most of Europe, per the [formats discipline](/news/date-currency-format-localization/)).
- **Design for the longest language.** German row labels run 25–35% longer than English ([expansion rules](/news/text-expansion-translation-layout/)); if the English layout is already full-bleed, German *will* wrap a label onto its value's line. Build 30% slack into label columns or use a condensed weight from the start.
- **One page means one page.** A datasheet that spills to two pages in French has failed — buyers staple, scan, and forward single pages. Set hard character budgets per block during translation rather than shrinking type afterward; the [vendor brief](/news/localization-vendor-brief-template/) has a field for exactly this.
- **Footnotes and legal lines** (certifications, disclaimers) are regulatory text — translate them with the same care as body copy; a mistranslated certification footnote is a compliance problem, not a typo.

## Manuals: structure carries the meaning

Manuals are worked through sequentially, often in bad light, under time pressure, by someone holding a wrench. The DTP rules follow from that:

- **Warnings never reflow.** Safety notices (DANGER/WARNING/CAUTION) must keep their icon, box, and *page position relative to the step they govern*. Text expansion that pushes a warning away from its procedure step is a liability defect — set keep-with-next constraints and verify page breaks in every language.
- **Numbered procedures must renumber cleanly.** Step lists, figure references ("see Fig. 4b"), and cross-references ("as described in section 7.2") break silently when translation changes pagination. Use cross-reference fields, never typed numbers — and run a link/x-ref check as a QA gate. This is where [structured authoring tools](/news/indesign-vs-framemaker-multilingual/) earn their keep.
- **Illustration callouts** (the 1, 2, 3 bubbles on exploded diagrams) stay numeric — but their legend text expands. Leave legend space for +40%, or move legends below the figure as a table.
- **Keep the source's information architecture identical across languages.** A French technician and an English one must be able to discuss "step 14 on page 38" — pagination parity is a feature, so choose fonts and spacing that preserve it. The full workflow is in our [manual translation checklist](/news/technical-manual-translation-dtp-checklist/).

## Catalogs: the grid is the brand

Catalogs are sales documents masquerading as reference documents. Hundreds of products, rigid grids, and photography doing the persuading:

- **Product-name length is the constraint.** German compound product names are the classic grid-breaker; CJK names are shorter but need the [font-pairing decisions](/news/cjk-latin-font-pairing/) to look intentional. Set name-field character budgets per product tier before translation.
- **Price/spec columns use tabular figures** and fixed-width alignment in every language; a column of ragged prices reads as unprofessional in any market.
- **Index and part-number ordering changes per language.** Alphabetical indexes reorder by translated names (and by locale collation rules — ä sorts differently in German and Swedish); rebuild indexes per language, don't just translate entries.
- **One template, many languages** — catalogs justify the investment in a master template with language layers, because they re-issue quarterly. The [translation memory economics](/news/translation-memory-dtp-efficiency/) are best here: a re-issue with 15% changed content should cost 15% of the original DTP, not 100%.

## The comparison at a glance

| Rule | Datasheet | Manual | Catalog |
|---|---|---|---|
| Primary constraint | Single-page fit | Pagination parity | Grid integrity |
| Expansion strategy | Character budgets | Reflow with keep-rules | Name-field budgets |
| Untranslatable elements | Values, units | Warnings' position, step numbers | Part numbers, prices |
| QA focus | Table alignment | X-refs, warnings, breaks | Index order, grid overflow |
| Re-issue cadence | Per product update | Rare, versioned | Quarterly — TM pays off |

## The shared rules

Whatever the type: translate in the layout tool or with layout-aware previews (never blind in spreadsheets for final files); keep fonts with the language coverage the [publishing pipeline](/news/multilingual-dtp-typography-guide/) requires; and proof *in the final PDF* — line breaks change meaning, and only a rendered page shows them. For scanned or un-editable sources, rebuild first per the [PDF workflow](/news/pdf-translation-workflow-editable/) rather than typesetting over patches.

Different documents fail differently — and the failures are all preventable at template time. Our [DTP team](/services/localization/dtp/) maintains language-ready templates for all three document types, with character budgets, keep-rules, and per-language indexes built in. [Send us one of each](/contact/) and we'll tell you where your current templates will break in German, French, and Arabic.
