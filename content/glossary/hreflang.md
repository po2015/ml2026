---
title: "hreflang"
definition: "The HTML attribute that tells search engines which language and region a page targets, so each visitor finds the version written for them."
description: "The HTML attribute that tells search engines which language and region a page targets, so each visitor finds the version written for them."
date: 2026-10-04
related:
  - ["International SEO guide", "/news/international-seo-guide-chinese-manufacturers/"]
  - ["Website building", "/services/website-building/"]
---

hreflang is an HTML attribute (or HTTP header, or sitemap entry) that declares the language — and optionally the region — a page is written for. When your site has an English page for the US, a Spanish page for Mexico, and an Arabic page for Saudi Arabia, hreflang tells Google which one to show to which searcher.

Without it, search engines guess. The result is familiar to many exporters: the English page outranks the local-language one in the target market, buyers bounce because they landed in the wrong language, or Google treats near-identical pages as duplicate content and ranks neither.

A correct implementation links every language version of a page to every other, including a self-reference and an x-default fallback for everyone else. The annotations must be reciprocal — if page A points to page B, page B must point back — and the URLs must match the canonical URLs exactly.

hreflang is not a ranking booster; it is a routing instruction. It does not make pages rank higher — it makes the right page rank in the right market. Every multilingual website MediaLocalize builds ships with validated hreflang across all language versions, checked again after every content update.
