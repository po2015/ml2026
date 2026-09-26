---
title: "Re-Translate or Update? Version Control for Translations"
date: 2027-05-10T12:18:00+08:00
publishDate: 2027-05-10T12:18:00+08:00
category: "industry"
category_label: "Industry"
tags: ["Localization", "version control", "content management", "translation workflow"]
keywords: ["translation version control", "translation update workflow", "multilingual document versions"]
cover: "/images/news/multilingual-content-version-control.jpg"
author: "MediaLocalize Team"
summary: "The manual changed: three sentences updated, one warning added, a spec revised. Do you re-translate the whole document in five languages, patch the changed sentences by hand, or just update the English and hope nobody notices? Without version control for translations, every content change forces a bad choice. How translation-memory-based change management turns re-translation into a pay-per-delta operation."
---

An engineering change ripples through a manufacturer's documentation: a torque spec updated, a safety warning reworded, a new accessory added. The English master documents are revised in a day. Then the translation question lands, and it's surprisingly awkward: the German manual is a 120-page InDesign file whose text was translated two years ago by a vendor nobody still works with. Options: re-translate everything (weeks, full price, five languages), have someone "just patch the changed bits" in each language (by whom, with what quality control?), or ship English-only updates and let the other languages drift (the quiet default, and how multilingual documentation dies). The uncomfortable truth: the cost of the *change* isn't the translation — it's the absence of a system that knows what changed and what survived. With version control plus translation memory, that three-sentence change costs three sentences, in every language, every time.

## Why translation without version control always degrades

The failure pattern is mechanical:

1. **Changes arrive continuously** — specs, regulations, product names, pricing, legal boilerplate. Documentation is never "done."
2. **Each change requires knowing exactly what changed** at sentence level, per language. Without tracked versions and a TM, nobody knows — so teams either over-pay (re-translate everything) or under-pay (hand-patches of unknown quality, or English-only drift).
3. **Drift compounds invisibly.** The German manual misses change #4, then #7, then #11. A year later it's a different document describing an older product — and the [liability isn't theoretical](/news/compliance-training-translation-accuracy/) when the drifted content is safety warnings.
4. **Hand-patching corrupts the TM asset.** Ad-hoc edits made inside layout files never return to the translation memory, so the next project re-translates those sentences anyway and terminology diverges — the [TM economics](/news/translation-memory-dtp-efficiency/) run in reverse.

## The working system: four components

**1. Source files in structured, diff-able formats.** Word and InDesign binaries diff poorly; the reason modern pipelines run on XML/DITA, Markdown, HTML, or XLIFF is that a computer can compare version N and N+1 and list changed segments exactly — the same argument as [structured technical documents](/news/technical-document-dtp-rules/) and [XML publishing](/news/automated-multilingual-publishing-xml/), seen from the maintenance side.

**2. Translation memory as the version store.** A well-maintained TM already holds every approved sentence pair. When version N+1 arrives, the TM match report *is* the change analysis: 100% matches = unchanged (free), fuzzy matches = changed (review at discount), no-match = new (translate). You pay for the delta, precisely.

**3. A defined change-propagation rule.** The [content sync discipline](/news/multilingual-content-sync-maintenance/) applied to documents: no source-language change ships without a translation work order for the affected segments, with a defined SLA per content criticality (safety/legal: before release; general: next batch). This single rule prevents drift — everything else is tooling.

**4. Version identifiers that survive contact with reality.** Every document and language version carries a visible version (Rev 3.2, 2027-05) tied to the source version it reflects. A distributor holding German Rev 3.0 against English Rev 3.2 knows exactly how stale it is; support can quote versions; audits can verify currency.

## The re-translate vs. update decision matrix

| Situation | Right move |
|---|---|
| Sentence/paragraph-level changes, TM exists, same vendor pipeline | **Update via TM** — translate the delta only |
| Restructured document (sections moved, heavy rewrites) | TM still applies at segment level; expect 60–85% matches — still far cheaper than from scratch |
| Source has no TM history (legacy vendor, lost assets) | **Align once**: build a TM from the existing source+translation pair ([alignment is a one-time salvage operation](/news/translation-memory-dtp-efficiency/)), then update via TM forever after |
| Translation quality was poor to begin with | Don't patch a bad asset — re-translate against the current [style guide](/news/translation-style-guide-brand-voice/) and termbase, *then* put it under version control |
| Layout changed but text didn't | No translation needed at all — the TM reimports into the new layout untouched; only the [DTP pass](/news/multilingual-dtp-typography-guide/) recurs |

The universal rule underneath: **never throw away an approved translation.** Even a full re-translation project should pre-translate from the existing TM and termbase first — approved sentences are assets, and assets get reused, not redone.

## Setting it up, pragmatically

1. **Inventory the documents that change** (catalogs, manuals, datasheets, legal pages) and their current language versions — including the orphaned ones with no TM history.
2. **Salvage the legacy assets**: align existing source/translation pairs into a TM (a service any professional [localization partner](/services/localization/) offers), and extract your [terminology](/news/terminology-management-termbase/) while you're at it.
3. **Move change-prone documents into diff-able formats** at their next natural revision — don't convert everything at once; convert what changes.
4. **Adopt the propagation rule** and put it in writing: criticality tiers, SLAs, and the named owner who triggers translation work orders when source content changes.
5. **Version-stamp everything**, visibly, in every language.

The payoff compounds: the second update costs a fraction of the first, the tenth update is routine, and the five-language documentation set stays *one product* instead of five snapshots diverging in slow motion.

Re-translation is a decision you should make rarely and deliberately — not the default forced by missing infrastructure. Our [localization team](/services/localization/) runs versioned translation pipelines: TM salvage and alignment, change-based pricing, propagation SLAs, and versioned delivery in every format from InDesign to XML. [Show us your document set](/contact/) and we'll estimate what your last year of updates *should* have cost.
