---
title: "The Website Localization Workflow: Audit to Launch"
date: 2026-10-20T08:29:00+08:00
publishDate: 2026-10-20T08:29:00+08:00
category: "industry"
category_label: "Industry"
tags: ["website localization", "localization workflow", "multilingual website", "project management"]
keywords: ["website localization process", "website localization workflow", "localization project steps"]
cover: "/images/news/website-localization-workflow.jpg"
author: "MediaLocalize Team"
summary: "What actually happens between 'we need a German website' and launch day: the eight phases of a professional website localization project, with realistic timelines."
---

"We need our website in German by Q2" sounds like a translation request. It is actually a small engineering project: content has to be audited, extracted, translated, reviewed, reintegrated, tested, and launched without breaking the site that is already generating inquiries. Companies that understand the workflow get realistic quotes and smooth launches; companies that think it is "just translation" get surprises.

Here is the eight-phase workflow we run for website localization, what happens in each phase, and where projects usually go wrong.

## Phase 1: Audit and scoping (week 1)

Before anything is translated, the source site is audited:

- **Content inventory**: which pages exist, which get traffic, which convert. A 200-page site often has 40 pages that matter — localizing everything is the most common budget waste.
- **Technical assessment**: CMS and URL structure, how content is stored (database, templates, hardcoded strings), whether the theme supports the target language's script and direction.
- **Asset inventory**: images with embedded text, PDFs, videos, downloadable documents — everything that also needs a localized version.

The output is a scope document: page list, word counts, asset list, and technical requirements. Every honest quote is built on this. If a vendor quotes without auditing, the number is fiction — our [vendor brief template](/news/localization-vendor-brief-template/) shows what to prepare so this phase goes fast.

## Phase 2: Internationalization fixes (week 1–2, parallel)

Problems found in the audit get fixed on the source site *before* translation starts, because every fix is cheaper in one language than in five:

- Hardcoded strings moved into translatable resources
- Date, currency, and unit formatting made locale-aware
- Layout adjusted to tolerate 30% text expansion (German) and right-to-left rendering (Arabic)
- Forms fixed to accept international names, addresses, and phone numbers

Skipping this phase is why translated sites ship with clipped buttons and English error messages.

## Phase 3: Glossary and style guide (week 2)

Two small documents prevent most quality arguments later:

1. **Terminology glossary**: your product names, technical terms, and industry vocabulary with approved translations — especially terms that must stay in English (brand names, model numbers) or follow market conventions.
2. **Style guide**: tone (formal Sie vs. informal du in German), number and date formats, how to handle untranslatable marketing phrases, legal phrasing requirements.

This is the phase clients most often want to skip and most often wish they had not. Fifteen terms agreed now saves three review rounds later.

## Phase 4: Translation (weeks 2–5)

Content moves into a translation management system where linguists work with translation memory (TM) — previously translated segments are reused, keeping terminology consistent and cutting cost on repeated content like product specs and legal text.

The method depends on content type:

- **Marketing pages (homepage, product overviews)**: professional human translation, often with a second linguist reviewing — this copy sells, and awkward phrasing here costs inquiries.
- **Long-tail content (news archives, FAQs, documentation)**: [machine translation with post-editing (MTPE)](/news/what-is-mtpe-post-editing/) is usually the right cost-quality balance.
- **Never raw machine translation** on buyer-facing pages; the quality difference is visible to any native speaker.

## Phase 5: Review and linguistic QA (week 4–6)

Translated content is reviewed in context — in a staging environment or screenshots, not in a spreadsheet. Reviewers check:

- Terminology against the glossary
- Register and tone per the style guide
- In-context fit: does that navigation label still make sense at its actual length, in its actual position?
- Numbers, units, links, and cross-references intact

Client-side review by your regional distributor or sales team slots in here. Give reviewers the glossary and a deadline; open-ended "take a look" is where projects stall for months.

## Phase 6: Integration and layout (week 5–6)

Approved translations go back into the site. This is engineering work, not copy-paste:

- Text expansion handled per component: buttons, navigation, tables, forms
- Fonts verified for the target script (CJK, Arabic, Cyrillic) — see our [multilingual typography guide](/news/multilingual-dtp-typography-guide/)
- Localized images, screenshots, and downloadable documents swapped in
- hreflang annotations, localized meta titles/descriptions, and language switcher wired up

## Phase 7: Functional and linguistic testing (week 6–7)

The staging site gets two parallel passes:

- **Functional**: every form submits, every link resolves, search works with non-Latin input, the language switcher preserves the current page, checkout/inquiry flows complete in each language.
- **Linguistic**: native speakers click through real user journeys looking for truncations, encoding issues (mojibake), mixed-language fragments, and untranslated strings.

Testing only in the source language and assuming the rest works is the classic failure — Arabic layouts and CJK input fields break in ways English testing never reveals.

## Phase 8: Launch and post-launch (week 7–8)

Launch is DNS-level boring if the earlier phases were done right. The work shifts to search:

- Submit localized sitemaps to Google Search Console (and Bing, Yandex, or Naver where relevant)
- Verify hreflang clusters resolve correctly
- Monitor indexation of the new language section over 2–4 weeks
- Set up per-language analytics views so each market's performance is visible from day one

## Realistic timelines

| Site size | Languages | Typical duration |
|---|---|---|
| 20–40 pages | 1 language | 4–6 weeks |
| 20–40 pages | 3–4 languages | 6–8 weeks (phases parallelize) |
| 100+ pages with docs/downloads | 1 language | 8–12 weeks |

Rush timelines are possible — by narrowing scope, not by skipping QA. Localizing 15 core pages well beats 60 pages badly, and the rest can follow in a second wave.

## Where projects go wrong

The failure modes are consistent across companies: quoting without an audit, translating before internationalization fixes, no glossary, review without deadlines, and testing only in English. Every one of them is a workflow problem, not a translation problem — which is why the workflow is the thing to evaluate when you choose a vendor.

If you are planning a multilingual site, our [localization team](/services/localization/) runs this exact workflow and can scope your project from a free audit — [start the conversation](/contact/), we respond within one business day.
