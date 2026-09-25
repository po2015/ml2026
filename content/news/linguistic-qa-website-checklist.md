---
title: "Linguistic QA for Translated Websites: The Checklist"
date: 2027-02-09T13:43:00+08:00
publishDate: 2027-02-09T13:43:00+08:00
category: "industry"
category_label: "Industry"
tags: ["localization", "linguistic QA", "website translation", "quality"]
keywords: ["linguistic qa website", "lqa checklist translation", "website translation quality check"]
cover: "/images/news/linguistic-qa-website-checklist.jpg"
author: "MediaLocalize Team"
summary: "The translation was perfect — in the spreadsheet. On the live site, the German navigation wraps, half the alt text is still English, and the checkout says 'Vielen Dank' on an Arabic page. Website LQA is a distinct pass with its own checklist. Here's the one we run."
---

A localization project ends with a delivery: translated files, reviewed, signed off. Then the site goes live and reality arrives — strings that made sense in a spreadsheet sit in the wrong context, a button truncates, the French version of one page links to the English version of the next. This gap exists because translation review checks *text*, while users experience *pages*. Linguistic QA (LQA) is the in-context pass that closes the gap: a native reviewer walks the live (or staging) site against a checklist, hunting the defects that only exist in context. Here is the checklist, in the order we run it — and the process decisions that determine whether it catches things.

## Why spreadsheet QA isn't enough

Three defect classes are invisible outside the running site:

- **Context errors**: "Home" translated as 主页 (correct for a homepage) where it's actually a breadcrumb meaning something else; "Return" as a keyboard key vs. a product return. The translator saw a string; the user sees a sentence.
- **Assembly errors**: translated fragments grammatically stitched by code — "Showing 1–10 of 247 results" rebuilt per language's word order, or not rebuilt and mangled. The [UI string discipline](/news/elearning-ui-text-expansion/) from course players applies to websites exactly.
- **Coverage gaps**: the strings nobody exported — alt text, meta descriptions, form validation messages, error pages, email templates, PDF downloads. Each was translated *somewhere* or wasn't; LQA is where you find out which.

## The checklist, pass by pass

Run as three focused passes rather than one blurry one. Each pass needs roughly an hour per 50 pages.

**Pass 1 — Language coverage (any reviewer, no linguistics needed).**
Hunt for untranslated content: navigation, footer, buttons, form labels *and* their error messages, alt text (inspect or screen-reader), meta titles/descriptions (view source or a crawler), 404/maintenance pages, transactional emails triggered by a test form submission, and downloadable assets. Rule: every string a user can see or a search engine can index is in scope. This pass alone typically surfaces 60% of findings on a first-time LQA.

**Pass 2 — Layout and rendering (reviewer + browser tools).**
- Truncation and overflow: buttons, menu items, cards, table headers — especially German/Finnish compounds, per the [expansion rules](/news/text-expansion-translation-layout/).
- Line-break disasters: headlines wrapping mid-word, orphan words in hero sections.
- Fonts: missing glyphs (tofu boxes), fallback fonts that change the design's tone — the [font-pairing problems](/news/cjk-latin-font-pairing/) made visible.
- RTL where applicable: mirrored layout, correct arrow directions, per the [RTL checklist](/news/rtl-website-design-arabic/).
- Numbers, dates, currencies: 01/02/2027 ambiguity, decimal commas, thousand separators — the whole [formats discipline](/news/date-currency-format-localization/) verified *rendered*, not assumed.

**Pass 3 — Linguistic in-context review (native reviewer).**
- Context correctness: does each string mean the right thing *here*? Buttons, CTAs, error messages, legal text.
- Terminology consistency: same product term across pages, matching the glossary and [translation memory](/news/translation-memory-dtp-efficiency/) — LQA is where TM drift shows.
- Register and voice: formal/informal consistency (German Sie, Spanish usted), tone matching the brand.
- Links: do internal links stay within the language, or leak to English? Language switcher lands on the *equivalent* page, not the section root?
- SEO elements: translated titles/descriptions, correct [hreflang behavior](/news/hreflang-mistakes-multilingual-b2b/), localized slugs where the architecture has them.

## The severity scale (so fixes actually ship)

| Severity | Definition | Example | Action |
|---|---|---|---|
| **S1 blocking** | Wrong meaning, legal/brand risk, broken transaction | Error message says the opposite; price formatted as 10× | Fix before launch, no exceptions |
| **S2 major** | Visible quality damage on key pages | Truncated CTA on homepage; English alt text on product images | Fix before launch |
| **S3 minor** | Polish issues on secondary pages | Inconsistent synonym on a blog archive page | Fix in next content cycle |
| **S4 suggestion** | Reviewer preference, not an error | "I'd phrase this headline differently" | Log; decide once, update glossary |

Without severities, LQA reports become 300-item lists nobody acts on. With them, the launch decision is mechanical: zero S1/S2 open = ship.

## Process rules that make it work

1. **LQA on staging, in the real CMS** — not on screenshots. Reviewers must click, submit forms, and trigger error states. Screenshot QA misses the interactive half of the site.
2. **Findings go back to assets, not just to pages.** Every terminology fix updates the glossary and TM; every recurring truncation updates the design system's string budgets; every missed context note improves the [vendor brief](/news/localization-vendor-brief-template/) for next time. Otherwise you pay for the same findings every release.
3. **One reviewer per language with authority.** LQA by committee stalls; one native reviewer with the power to mark S1–S4 keeps it to days, not weeks.
4. **Re-run the cheap passes every deploy.** Pass 1 (coverage) and the layout half of Pass 2 can be largely automated with a crawler and screenshot diffing — run them on every release; save human linguists for Pass 3.
5. **Budget it.** LQA runs 10–15% of translation cost and catches the defects that would otherwise be found by your *customers*, in public. It's the same insurance logic as [pseudolocalization](/news/pseudolocalization-testing-guide/) upstream — cheap certainty versus expensive embarrassment.

Translation makes your site multilingual; LQA makes it *believable*. Our [localization team](/services/localization/) builds in-context LQA into every website project — native reviewers, severity-triaged findings, and fixes that flow back into your glossary and TM. [Send us your staging URL](/contact/) and we'll run Pass 1 on it as a free audit.
