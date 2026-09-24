# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Hugo static site for medialocalize.com (B2B AI website building + localization services). No JavaScript build step, no package.json, no test or lint tooling — the entire site is Hugo templates, Markdown content, and one JSON data file.

## Commands

- Dev server: `hugo server` (add `-D` to include drafts)
- Production build: `hugo --gc --minify` (outputs to `public/`, which is gitignored — a stale local copy may exist but is never committed)
- New content: `hugo new content/news/my-post.md` (archetype sets `draft = true`)
- Hugo version: extended **0.157.0** (pinned in `.github/workflows/hugo.yml`; match it locally)

Deployment: push to `main` triggers GitHub Actions → GitHub Pages. There is also `functions/api/contact.js`, a Cloudflare Pages Function (contact form → Feishu webhook via `FEISHU_WEBHOOK` env var, with `_hp` honeypot / `_t0` timing bot guards) — keep its client-side form in sync if you edit either side.

## Architecture

### Custom i18n system (the most important thing to understand)

The site has 5 languages — `en` (default, at root), `zh`, `es`, `ru`, `ar` (RTL, in subdirs) — but does **not** use Hugo's `i18n/` string tables (that directory is empty). Instead:

- **All UI and page copy lives in `data/site_i18n.json`**, keyed by language, then by section (`meta`, `nav`, `pages`, ...).
- Every page template starts with `{{- $copy := partial "i18n/site.html" . -}}` (current language's dict, falls back to `en`).
- `partials/i18n/page.html` derives a lookup key from the content file path (`content/services/localization/dtp/_index.md` → `services/localization/dtp`) and returns `$copy.pages[$key]`. `i18n/title.html` / `i18n/description.html` let this JSON override the page's front-matter title/description.

**Consequence:** most content Markdown files are thin shells (front matter + little body text). To change what a page actually says, edit `data/site_i18n.json` — and edit it for **all five languages**, not just English. When adding a new page, add its copy under a matching `pages` key in every language block.

### Content layout

Each page exists as 5 sibling files: `name.md` (English) plus `name.zh/es/ru/ar.md`. Section pages are `_index` bundles; `content/services/localization/` nests four sub-services (`dtp`, `dubbing`, `elearning`, `video`). When adding a page, create all five variants.

### Theme (`themes/ml`)

- Custom per-page templates: a page sets `layout: "<name>"` in front matter, resolved against `themes/ml/layouts/<section>/<name>.html` (e.g. `layout: "localization"` → `layouts/services/localization.html`; `contact` uses `contact/list.html`). Service sub-pages each have a dedicated template (`services/dtp.html`, etc.) containing substantial hardcoded markup — check both the template and `site_i18n.json` when editing a service page.
- `_default/baseof.html` wires `<html lang dir>` from the i18n copy (handles Arabic RTL), plus nav/footer/scroll-reveal partials.
- CSS/JS: `themes/ml/assets/css/main.css`, `assets/js/main.js` (no pipeline beyond Hugo's asset handling).

### Reference documents (not loaded by Hugo)

- `apple-design/DESIGN.md` — the design system the theme implements (Apple-style: SF Pro typography, black/`#f5f5f7` alternating sections, single accent `#0071e3` reserved for interactive elements). Follow it when adding new sections/pages; `preview.html` shows it rendered.
- `company.yaml` — business source-of-truth: service definitions, three-tier USD pricing for website packages, site architecture. Consult it when editing the prices or services pages.
- `prepare.md` / `requirment.md` — original project briefs (in Chinese).

### Hugo config notes (`hugo.toml`)

- All languages share `contentDir = "content"`; translations link purely by filename suffix.
- Taxonomies: `tags` and `category`; related-content weighting is configured (tags > category > date).
- Goldmark `unsafe = true` — raw HTML in Markdown is rendered.
