---
title: "多语言 B2B 网站上的 Hreflang 错误（以及修复方法）"
date: 2026-10-19T16:52:00+08:00
publishDate: 2026-10-19T16:52:00+08:00
category: "tech"
category_label: "技术洞察"
tags: ["SEO", "hreflang", "多语言网站", "技术 SEO"]
keywords: ["hreflang 实施", "hreflang 错误", "多语言 SEO"]
cover: "/images/news/hreflang-mistakes-multilingual-b2b.jpg"
author: "MediaLocalize Team"
summary: "Hreflang 是国际 SEO 中被错误实施最多的标签。我们在 B2B 网站上最常发现的六个错误，如何发现它们，以及逐一的修复方法。"
---

Hreflang 的想法很简单：告诉 Google 该向哪个搜索者展示哪个语言版本的页面。但在实践中，它是国际 SEO 中被持续错误实施的元素——对多语言网站的审计通常会在大多数页面上发现 hreflang 错误，Google 自己的文档也称其为国际定向中最复杂的方面之一。

做错的代价对 B2B 来说很具体：你的德国潜在客户搜索之后，拿到的是英文页面（或者更糟，你的西班牙文页面），还没读一个字就跳出去了。本文覆盖我们在多语言 B2B 网站上最常发现的六个错误、如何排查每一个，以及修复方法。

## hreflang 本应做什么

每个页面声明自己的语言以及各替代版本的 URL:

```html
<link rel="alternate" hreflang="en" href="https://example.com/products/valve/">
<link rel="alternate" hreflang="de" href="https://example.com/de/products/valve/">
<link rel="alternate" hreflang="zh" href="https://example.com/zh/products/valve/">
<link rel="alternate" hreflang="x-default" href="https://example.com/products/valve/">
```

Google 把这些标注作为提示，在搜索结果中替换 URL，让搜索者落到对应语言的版本上。有两个特性让它很脆弱：**标注必须是双向的**（如果页面 A 指向页面 B，页面 B 必须指回 A)，而且**簇中任何一条断链都可能让整组标注失效**。

## 我们最常发现的六个错误

### 1. 缺少回链

目前最常见的错误。英文页面列出了所有替代版本，但翻译页面一个都不列——或者指向的 URL 与指向它们的那条不一致。没有双向确认，Google 会忽略这些标注。

**症状**:Google Search Console 报告 "Alternate page with proper canonical tag"（具有规范标签的替代页面），或者干脆从不替换 URL；翻译页面很少出现在本地搜索结果中。
**修复**：集中生成 hreflang 标注——从你的 CMS、站点地图生成器或构建系统——而不是按语言逐个编辑模板。簇中任何一个页面都必须列出所有成员，包括它自己。

### 2. 语言或地区代码错误

`en-UK` 而不是 `en-GB`,`zh-CH` 而不是 `zh-CN`,`jp` 而不是 `ja`（代码指语言，不是国家）。同样常见的是：只用一个地区代码（`de` 是合法的；单写 `DE` 作为语言不是合法的 hreflang 值——hreflang 接受语言或语言+地区，绝不接受单独的地区）。

**症状**:Search Console 旧版国际定向报告报错；第三方爬虫标记非法值。
**修复**：用 ISO 639-1（语言）和 ISO 3166-1 Alpha 2（地区）校验每一个代码。拿不准时，只用语言代码（`de`)——它定向的是全世界讲德语的人，这通常正是 B2B 网站想要的。

### 3. 在非规范或被 noindex 的页面上使用 hreflang

标注指向的 URL 发生了重定向、被 canonical 到了另一个 URL，或带着 `noindex` 标签。Google 跟随 canonical，发现的是另一个页面，于是丢弃这个信号。这在网站改版后不断发生：hreflang 模板还指着旧 URL。

**症状**:"Duplicate, Google chose different canonical"（重复内容，Google 选择了不同的规范页）覆盖率问题；标注被悄悄丢弃。
**修复**:hreflang 的 URL 必须是最终的、规范的、可索引的、返回 200 状态的 URL。任何 URL 变更之后，重新生成整套 hreflang——局部更新正是这类错误持续多年的原因。

### 4. x-default 损坏或缺失

`x-default` 告诉 Google：对于你不覆盖的语言，把搜索者送到哪里。网站要么干脆省略它，要么把它指向一个本身内容单薄的语言选择页。没有它，Google 只能猜——而当买家用比如法语搜索、而你只有英语、德语和中文版本时，它常常猜错。

**症状**：对未覆盖的市场，出现"错误的"语言版本。
**修复**：把 `x-default` 指向你的主要全球版本（通常是英文）。语言选择页也可以接受，但前提是它是一个真实的、可索引的页面。

### 5. hreflang 簇与内容不匹配

每个簇应该连接的是**等价页面**——同一个产品页的五个语言版本。常见的违规：把德语"产品"页标注为英文*类目*页的替代版本；或者把从未创建的翻译页面列进标注，返回 404。

**症状**:Google 把用户换到一个与其查询意图不匹配的页面——本地化页面的跳出率攀升。
**修复**：只标注真正的等价页面。如果某个页面只有英文版，它就构成一个只有一名成员的簇——只列它自己（加上 x-default)，而不是指向一个"差不多"的页面。

### 6. 信号冲突：hreflang、canonical 与重定向打架

英文页 canonical 到德语页（"它们内容基本一样")，而 hreflang 却说它们是不同的替代版本。或者地理位置重定向不管美国访客点了什么，都强制把他们送到 `/en/`——这同样会重定向 Googlebot，让它根本爬不到你的其他语言版本。

**症状**：整个语言板块从索引中消失。
**修复**:canonical 应该在每个语言版本内部自指；跨语言的工作交给 hreflang。永远不要按 IP 硬重定向——改为显示一个可关闭的语言建议横幅，这样 Googlebot（从美国 IP 爬取）仍然能到达每个版本。

## 快速诊断表

| 错误 | 最快的排查方法 |
|---|---|
| 缺少回链 | 用 Screaming Frog 爬一遍；对比每个页面发出的标注与指向它的标注 |
| 代码错误 | 任何 hreflang 校验器，或爬虫的非法值报告 |
| 非规范目标 | 检查每个被标注的 URL 返回 200 且 canonical 自指 |
| 缺少 x-default | 查看首页源代码 |
| 等价页面不匹配 | 跨语言手工抽查十个簇 |
| 重定向冲突 | 从美国 IP 爬一遍，确认所有语言版本都可达 |

## 修复后如何验证

1. **全站爬取**并导出所有 hreflang 标注；双向性和合法性的错误会立刻出现在工具的报告中。
2. **在接下来的几周里观察 Search Console 覆盖率**中受影响的语言板块——一旦标注一致，翻译页面上常见的 "Crawled, currently not indexed"（已抓取，暂未编入索引）往往会消除。
3. **像你的买家一样搜索**：用 `site:example.com/de/` 加上一个德语产品词，从德国 IP（或 VPN）验证出现的是德语 URL。

## 什么时候你可能不需要 hreflang

如果你的网站每个市场恰好一种语言，且每种语言住在自己的 ccTLD 上（`example.de` 放德语）,Google 的地理信号已经足够强——hreflang 仍然推荐，但出错时伤害较小。hreflang 最重要的场景，恰恰是大多数出口商实际使用的架构：**一个 `.com` 加语言子目录**，此时 Google 没有别的办法知道哪个版本服务哪个搜索者。如果这是你的架构，正确的 hreflang 就不是可有可无的装饰——它是把正确的页面送到正确买家面前的机制。

把标注做对是一次性的工程任务，回报是永久的。我们的[网站建设团队](/zh/services/website-building/）在构建每一个出口网站时都会实施多语言 SEO 架构——hreflang、URL 结构和 Search Console 配置。[把你的域名发给我们](/zh/contact/)，我们会为它做一次免费的 hreflang 检查。
