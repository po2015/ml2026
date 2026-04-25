---
# ============================================================
# MEDIALOCALIZE NEWS ARTICLE TEMPLATE
# draft: true 确保此文件不会被 Hugo 渲染发布
# 复制本文件，修改文件名（slug），填写下方字段后开始写作
# ============================================================
draft: true
build:
  render: never
  list: never
  publishResources: false
# ---[ 必填字段 ]----------------------------------------------

# 文章标题：清晰描述主题，包含核心关键词，60 字符以内
title: "Article Title — Include Primary Keyword Here"

# 发布日期（ISO 8601 格式）
date: 2026-01-01

# 分类（category 用于过滤；category_label 用于显示）
# 可选值: tech | industry | company
category: "tech"
category_label: "Tech Insights"   # 或 "Industry" / "Company"

# 摘要：120–160 字符，用于列表页卡片和 meta description
# 应清楚说明读者能从文章获得什么，不要写成标题的重复
summary: "One or two sentences summarising what the reader will learn. Should stand alone without reading the article."

# ---[ 推荐填写 ]----------------------------------------------

# 封面图（显示在文章顶部，also used for OG image）
# 图片放在 /static/images/news/ 目录，建议尺寸 1200×630
cover: "/images/news/your-image.jpg"

# 作者姓名（显示在文章底部）
# 可选: Ken Lee | Jerry Hu | Jesse Chen | Benny Chow
author: "Ken Lee"

# 标签：用于 related articles 匹配和 SEO
# 建议 3–6 个，使用已有标签保持一致性
# 常用标签: DTP | InDesign | FrameMaker | CJK | Arabic | RTL |
#           AI Dubbing | Human Dubbing | Video Localization |
#           E-Learning | SCORM | Translation Memory | memoQ |
#           SEO | Website Building | Chinese-English | B2B Export
tags: ["Tag One", "Tag Two", "Tag Three"]

# ---[ 可选字段 ]----------------------------------------------

# 关键词（用于 meta keywords，补充 tags 之外的长尾词）
keywords: ["keyword one", "keyword two"]

# 最后修改日期（不填则自动取 git 修改时间）
# lastmod: 2026-01-15

# 是否在 sitemap 中排除（默认 false）
# sitemap_exclude: false

---

<!--
==============================================================
  ARTICLE WRITING GUIDE FOR AI
==============================================================

TARGET LENGTH: 900–1800 words (excluding frontmatter)
VOICE: Technical but accessible. No filler phrases.
       Write for B2B decision-makers in manufacturing, pharma,
       or training industries who are evaluating localization
       or website-building vendors.
LINK INTERNALLY: Link to relevant service pages (/services/...)
       and case studies (/cases/...) where natural.

--------------------------------------------------------------
  STRUCTURE TEMPLATE (H2 = section, H3 = subsection)
--------------------------------------------------------------
-->

Brief introductory paragraph (2–4 sentences). State the problem
or question the article addresses. No heading before the first
paragraph.

## H2: First Major Section

Section body paragraph. Keep paragraphs to 3–5 sentences.
Avoid padding.

### H3: Subsection (use when a section has 2+ distinct subtopics)

Subsection content.

Unordered list example:
- Item one — add a brief explanation after the dash when useful
- Item two
- Item three

Ordered list example (for steps or ranked items):
1. **Step name**: Explanation of this step in one or two sentences.
2. **Step name**: Explanation.
3. **Step name**: Explanation.

## H2: Second Major Section

### Comparison Table Example

| Column A | Column B | Column C |
|---|---|---|
| Row 1 A | Row 1 B | Row 1 C |
| Row 2 A | Row 2 B | Row 2 C |

## H2: Third Major Section

Image with caption example (Hugo renders raw HTML when unsafe = true):

<figure>
  <img src="/images/news/your-image.jpg" alt="Descriptive alt text" loading="lazy">
  <figcaption>Caption text: explain what the image shows and why it matters to the reader.</figcaption>
</figure>

Blockquote for notable quotes or pull quotes:

> "Quoted text here — an insight from a team member, client, or industry expert."
> — Name, Role

### Notice / Callout Blocks

Use sparingly — maximum one per 400 words.

**Info (neutral background information):**
<div class="notice notice-info">
<strong>Note</strong>
Supporting context the reader should be aware of, but that doesn't block them from proceeding.
</div>

**Tip (best practice or shortcut):**
<div class="notice notice-tip">
<strong>Tip</strong>
Actionable advice the reader can apply immediately.
</div>

**Warning (common mistake or caution):**
<div class="notice notice-warning">
<strong>Warning</strong>
Something the reader should check or verify before proceeding. Mistakes here cause rework or cost.
</div>

**Danger (critical issue, compliance, or irreversible risk):**
<div class="notice notice-danger">
<strong>Critical</strong>
A stop-and-read issue. Use only for genuinely high-stakes information.
</div>

---

Section divider (use `---` sparingly, between major topic shifts only).

## Conclusion / Final Section

Close with a practical takeaway or recommendation. End with a
call to action linking to /contact/ or a relevant service page.

Example closing line:
If [topic] is relevant to your current project, [talk to our team](/contact/) — we respond within one business day.

<!--
==============================================================
  CHECKLIST BEFORE SUBMITTING
==============================================================
[ ] Title includes primary keyword and is under 60 chars
[ ] Summary is 120–160 chars and stands alone
[ ] All H2 headings use sentence case (not Title Case)
[ ] At least one table or list in the article
[ ] At least one internal link to a service or case study page
[ ] cover image path is correct and image exists in /static/
[ ] tags match the article content (3–6 tags)
[ ] author field is set to a real team member name
[ ] No filler phrases ("In today's world...", "It goes without saying...")
[ ] Article has been spell-checked in the target language
==============================================================
-->
