---
title: "Hreflang Mistakes on Multilingual B2B Sites (And Fixes)"
date: 2026-10-19T16:52:00+08:00
publishDate: 2026-10-19T16:52:00+08:00
category: "tech"
category_label: "Tech Insights"
tags: ["SEO", "hreflang", "multilingual website", "technical SEO"]
keywords: ["hreflang implementation", "hreflang errors", "multilingual seo"]
cover: "/images/news/hreflang-mistakes-multilingual-b2b.jpg"
author: "MediaLocalize Team"
summary: "Hreflang is the most misimplemented tag in international SEO. The six mistakes we find most often on B2B sites, how to spot them, and how to fix each one."
---

Hreflang is a simple idea: tell Google which language version of a page to show which searcher. In practice, it is the most consistently misimplemented element in international SEO — audits of multilingual sites routinely find hreflang errors on the majority of pages, and Google's own documentation calls it one of the most complex aspects of international targeting.

The cost of getting it wrong is specific to B2B: your German prospect searches, gets the English page (or worse, your Spanish page), and bounces before reading a word. This article covers the six mistakes we find most often on multilingual B2B sites, how to check for each, and the fix.

## What hreflang is supposed to do

Each page declares its own language and the URLs of its alternates:

```html
<link rel="alternate" hreflang="en" href="https://example.com/products/valve/">
<link rel="alternate" hreflang="de" href="https://example.com/de/products/valve/">
<link rel="alternate" hreflang="zh" href="https://example.com/zh/products/valve/">
<link rel="alternate" hreflang="x-default" href="https://example.com/products/valve/">
```

Google uses these annotations as a hint to swap URLs in search results so searchers land on the version in their language. Two properties make it fragile: **annotations must be reciprocal** (if page A points to page B, page B must point back to A), and **a single broken link in the cluster can invalidate the whole set**.

## The six mistakes we find most often

### 1. Missing return links

The most common error by far. The English page lists all alternates, but the translated pages list none — or point to a different URL than the one that pointed to them. Without confirmation from both sides, Google ignores the annotation.

**Symptom**: Google Search Console reports "Alternate page with proper canonical tag" or simply never swaps URLs; translated pages rarely appear in their local search results.
**Fix**: generate hreflang annotations centrally — from your CMS, sitemap generator, or build system — rather than editing templates per language. Any page in a cluster must list every member, including itself.

### 2. Wrong language or region codes

`en-UK` instead of `en-GB`, `zh-CH` instead of `zh-CN`, `jp` instead of `ja` (the code is the language, not the country). Also common: using a region code alone (`de` is valid; `DE` alone as a language is not a hreflang value — hreflang takes language or language+region, never region alone).

**Symptom**: errors in Search Console's legacy international targeting report; third-party crawlers flag invalid values.
**Fix**: validate every code against ISO 639-1 (language) and ISO 3166-1 Alpha 2 (region). When in doubt, use the language code alone (`de`) — it targets German speakers worldwide, which is usually what a B2B site wants anyway.

### 3. Hreflang on non-canonical or noindexed pages

The annotation points to a URL that redirects, is canonicalized to another URL, or carries a `noindex` tag. Google follows the canonical, finds a different page than the one annotated, and discards the signal. This happens constantly after site migrations, when hreflang templates keep pointing at old URLs.

**Symptom**: "Duplicate, Google chose different canonical" coverage issues; annotations silently dropped.
**Fix**: hreflang URLs must be the final, canonical, indexable, 200-status URLs. After any URL change, regenerate the entire hreflang set — partial updates are how these errors persist for years.

### 4. Broken or missing x-default

`x-default` tells Google where to send searchers whose language you do not cover. Sites either omit it or point it at a language-selector splash page that itself has thin content. Without it, Google guesses — and often guesses wrong for buyers searching in, say, French when you only have English, German, and Chinese.

**Symptom**: the "wrong" language version appears for uncovered markets.
**Fix**: point `x-default` at your primary global version (usually English). A language selector page is also acceptable, but only if it is a real, indexable page.

### 5. Hreflang clusters that don't match the content

Each cluster should connect **equivalent pages** — the same product page in five languages. Common violations: the German "product" page annotated as an alternate of the English *category* page, or translated pages that were never created still listed in annotations, returning 404s.

**Symptom**: Google swaps users to a page that does not match their query intent — bounce rates climb on localized pages.
**Fix**: only annotate true equivalents. If a page exists only in English, it forms a cluster of one — list just itself (plus x-default), rather than pointing to a near-miss page.

### 6. Conflicting signals: hreflang vs canonical vs redirects

The English page canonicals to the German page ("they're basically the same content"), while hreflang says they are distinct alternates. Or geolocation redirects force US visitors to `/en/` regardless of what they clicked — which also redirects Googlebot and prevents it from crawling your other language versions at all.

**Symptom**: entire language sections drop out of the index.
**Fix**: canonicals should be self-referential within each language version; let hreflang do the cross-language work. Never hard-redirect based on IP — show a dismissible language suggestion banner instead, so Googlebot (crawling from US IPs) can still reach every version.

## Quick diagnostic table

| Mistake | Fastest way to spot it |
|---|---|
| Missing return links | Crawl with Screaming Frog; compare each page's outgoing annotations against incoming ones |
| Wrong codes | Any hreflang validator, or the crawl's invalid-value report |
| Non-canonical targets | Check every annotated URL returns 200 and canonicals to itself |
| Missing x-default | View source on the homepage |
| Mismatched equivalents | Manually spot-check ten clusters across languages |
| Redirect conflicts | Crawl from a US IP and confirm all language versions are reachable |

## How to test after fixing

1. **Crawl the full site** and export all hreflang annotations; errors of reciprocity and validity show up immediately in the tool's report.
2. **Check Search Console coverage** for the affected language sections over the following weeks — "Crawled, currently not indexed" on translated pages often clears once annotations are consistent.
3. **Search like your buyers**: use `site:example.com/de/` plus a German product term from a German IP (or a VPN) and verify the German URL appears.

## When you might not need hreflang

If your site has exactly one language per market and each language lives on its own ccTLD (`example.de` for German), Google's geographic signals are already strong — hreflang is still recommended but errors there are less damaging. Hreflang matters most for the setup most exporters actually run: **one `.com` with language subdirectories**, where Google has no other way to know which version serves which searcher. If that is your architecture, correct hreflang is not optional decoration — it is the mechanism that puts the right page in front of the right buyer.

Getting the annotations right is a one-time engineering task with permanent payoff. Our [website building team](/services/website-building/) implements multilingual SEO architecture — hreflang, URL structure, and search console setup — as part of every export site we build. [Send us your domain](/contact/) and we will run a free hreflang check on it.
