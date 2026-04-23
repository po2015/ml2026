---
title: "Multilingual DTP Explained: Typography Rules, Tools, and Workflow for Chinese-English Documents"
date: 2026-04-23
category: "tech"
category_label: "Tech Insights"
tags: ["DTP", "InDesign", "Typography", "CJK", "Chinese-English", "Document Localization"]
summary: "Getting multilingual DTP right is about more than swapping out text. This guide covers CJK typography rules, font selection, tool comparison, and the five-step workflow we follow on every technical document project."
cover: "/images/services/dtp.jpg"
author: "Jerry Hu"
---

Multilingual desktop publishing (DTP) is the discipline of taking a document — a product manual, a pharmaceutical brochure, an annual report — and rebuilding its layout so that the translated text fits, reads correctly, and meets the typographic standards of the target language. Translation ends when the words are converted. DTP begins right after.

For English-to-Chinese or Chinese-to-English projects, the challenges are significant: character set differences, text expansion or contraction, different punctuation conventions, and a completely different visual rhythm on the page. This guide covers the essentials.

## What Multilingual DTP Actually Involves

Most clients assume that translating a document is the hard part. In practice, the translated text arriving back into an InDesign or FrameMaker file is often the beginning of the real work.

### Why Text Volume Changes After Translation

Text length changes significantly between language pairs. Moving from Chinese to English typically **expands the word count by 30–50%**. The reverse journey — English to Chinese — contracts it. Either direction means the original layout breaks: text overflows its frame, captions no longer align with images, and page counts shift.

What a DTP engineer actually does on a typical project:

- Re-flows text frames to accommodate expansion or contraction
- Adjusts leading (line spacing), tracking, and kerning for readability in the target script
- Replaces source-language fonts with target-language equivalents, checking licensing
- Rebuilds tables where CJK text creates height-mismatched rows
- Verifies numbering, cross-references, and TOC entries after page count changes
- Exports to PDF/X-1a or PDF/X-4 for print, or interactive PDF for screen delivery

<figure>
  <img src="/images/services/localization.jpg" alt="Multilingual document localization workflow" loading="lazy">
  <figcaption>A typical multilingual DTP project handles parallel InDesign packages for each language, with linked image assets shared across all versions.</figcaption>
</figure>

## Choosing the Right Fonts

Font selection is the single most common cause of DTP rework. The wrong font choice affects readability, legal compliance (font licensing), and print output quality.

### Font Comparison by Use Case

| Use Case | Recommended CJK Fonts | Recommended Latin Fonts |
|---|---|---|
| Technical manuals (print) | Noto Sans CJK, Source Han Sans | Source Sans Pro, Helvetica Neue |
| Legal / pharmaceutical | Founder Fang Song, AR PL UMing | Times New Roman, Georgia |
| Marketing / brand | Custom brand CJK (if available), HanHei | Brand typeface |
| Screen / e-learning | Noto Sans CJK SC, PingFang SC | Inter, DM Sans |
| Mixed CJK + Latin inline | Source Han Sans (includes Latin) | — (use bundled Latin) |

<div class="notice notice-warning">
<strong>Font Licensing</strong>
Most system fonts (including Microsoft YaHei, SimSun, and DFKai-SB) are licensed for screen display only. Commercial print projects require a separately licensed version. Using system fonts in print-destined PDFs without a print license is a common compliance risk. Always verify with the font vendor before submitting files to a print provider.
</div>

## CJK Typography Rules

CJK (Chinese, Japanese, Korean) typography follows conventions that differ substantially from Latin typesetting. Applying Western rules to CJK text produces layouts that look technically correct but feel wrong to native readers.

### Line Spacing and Character Metrics

CJK fonts are designed on a full-width em-square. This means:

1. **Leading should be set to 150–175%** of the type size for body text. Tighter leading (120–130%) common in English layouts makes CJK body copy feel cramped.
2. **Tracking adjustments are rarely needed** for CJK — the built-in spacing of a well-designed CJK font is already calibrated for the script.
3. **Optical margin alignment** (hanging punctuation) behaves differently. CJK full-width punctuation (。，「」) occupies the full em-square and should not be pulled into the margin the way Latin punctuation can be.
4. **Hyphenation does not apply** to CJK. Line breaks happen after any character except opening brackets.
5. **Bold weights in CJK** are achieved by using a bold font variant, never by applying synthetic bold in InDesign — this degrades stroke quality at print resolution.

### Punctuation and Special Characters

CJK punctuation rules differ from English in ways that catch even experienced DTP engineers off guard:

- **Full-width vs. half-width**: CJK body text uses full-width punctuation (，。！？). Technical content (code, part numbers) uses half-width (,  .  !  ?). Mixing these in the same paragraph looks wrong.
- **Opening and closing quotation marks**: Simplified Chinese uses 「」or " ". Traditional Chinese uses「」. Japanese uses 『』for nested quotes. These are not interchangeable.
- **No space before or after punctuation** in Chinese — unlike English where a space follows every period or comma.

> "The most frequent mistake we see in CJK documents localized by non-specialist teams is applying English punctuation rules directly. It signals immediately to a Chinese reader that the document was not written for them."
> — Jerry Hu, Senior DTP Engineer

## Arabic and RTL Script Considerations

Arabic, Hebrew, Farsi, and Urdu documents present a different category of DTP challenges. The **entire layout must be mirrored**: text flows right-to-left, columns reverse, and images that were on the left in the source document typically move to the right in the RTL version.

<div class="notice notice-danger">
<strong>Critical: RTL Layout Is Not Just Text Direction</strong>
Setting paragraph direction to right-to-left in InDesign is not sufficient for a professional RTL layout. Page binding direction, master page column order, numbered list alignment, table cell padding, and running headers all need to be explicitly restructured. Attempting an RTL layout without a dedicated RTL-trained DTP engineer typically produces files that fail print preflight.
</div>

Key rules for Arabic DTP:

- Use **Adobe World-Ready Composer** (not the default Paragraph Composer) for all Arabic text
- **Kashida** (letter extension) is used for justification in Arabic — never use letter-spacing or word-spacing for justification
- Arabic text should never be set in **oblique/italic** — use a dedicated italic Arabic font variant if emphasis is required
- **Vowel diacritics** (tashkeel) require additional vertical space; Quranic text or formal Arabic prose needs 160–180% leading

## The 5-Step DTP Localization Workflow

Our standard workflow for multilingual DTP projects:

1. **Source file audit** — Verify that source files (InDesign IDML/INDD, FrameMaker FM/BOOK) are supplied with all linked assets, embedded fonts listed, and color profiles identified. Missing links at this stage cause delays later.
2. **Pre-translation prep** — Apply paragraph and character styles consistently; convert any manually-styled text to proper styles. This makes re-import of translated XLIFF content clean.
3. **Translation import** — Translated content is imported via XLIFF or direct copy, depending on the workflow. Text frames are checked for overflow immediately.
4. **Layout adjustment** — Re-flow frames, adjust leading and tracking, fix widow/orphan issues, rebuild tables, align cross-references and TOC.
5. **Preflight and export** — Run Acrobat or InDesign preflight against the delivery specification (PDF/X-1a for offset print, PDF/X-4 for digital print, interactive PDF for screen). Resolve all preflight errors before delivery.

<div class="notice notice-tip">
<strong>Tip: Invest in Styles Upfront</strong>
Source documents built with consistent paragraph and character styles — rather than manually-applied formatting — reduce DTP time by 25–40% per language version. If you commission recurring documents (product catalogs, annual reports), ask your DTP partner to help establish a style guide before the first project begins.
</div>

## Common Mistakes and How to Avoid Them

- **Embedding fonts that are not licensed for embedding** — check the Permissions tab in font info before including fonts in PDFs
- **Using bitmap images below 300 dpi for print** — screen exports at 72–96 dpi are not usable for offset or digital print
- **Applying western kerning pairs to CJK text** — this distorts CJK character spacing
- **Ignoring text expansion in UI strings** — buttons and labels in technical documentation often have tight containers; expansion into Chinese can truncate labels
- **Delivering live PDFs without flattened transparency** — transparency effects must be flattened for reliable output on older RIP systems
- **Not creating a language-specific color profile** — CMYK values for Pantone colors sometimes differ between print regions; Chinese printers commonly use GB 7705 color standards rather than FOGRA39

## Tool Comparison

| Tool | Best For | CJK Support | RTL Support | Collaboration |
|---|---|---|---|---|
| Adobe InDesign | Marketing, brand, editorial | Excellent (World-Ready Composer) | Good (ME edition) | CC Libraries |
| Adobe FrameMaker | Technical documentation, structured content | Good | Limited | Poor |
| QuarkXPress | Long-form print | Moderate | Good | Moderate |
| Microsoft Publisher | Low-complexity internal docs | Basic | None | SharePoint |
| Affinity Publisher | Budget alternative, shorter docs | Moderate | Limited | None |

For most client projects we work in InDesign. FrameMaker is preferred for structured technical documentation where the source is DITA XML or DocBook, as its structured editing capabilities eliminate manual re-import steps.

---

If your team regularly produces multilingual technical documents and you are not yet using paragraph styles, XLIFF-based translation workflows, or preflight automation — there is likely significant time and cost being left on the table. [Talk to our DTP team](/contact/) about auditing your current workflow.
