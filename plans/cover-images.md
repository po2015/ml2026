# 封面图来源记录（Pexels）

Pexels 许可：免费商用，无需署名。此处留存来源备查。

| 文章 slug | Pexels 图片 | 作者 |
|---|---|---|
| ai-website-builder-vs-custom-development | [photo 577585](https://www.pexels.com/photo/coding-computer-data-depth-of-field-577585/) | (Pexels) |
| international-search-engines-comparison | [photo 7927187](https://www.pexels.com/photo/a-desk-globe-beside-a-rolled-map-7927187/) | Nothing Ahead |
| how-many-languages-export-website | [photo 12672575](https://www.pexels.com/photo/international-flags-from-different-countries-hanging-in-the-street-12672575/) | Vlada Karpovich |
| how-ai-dubbing-works | [photo 270288](https://www.pexels.com/photo/grayscale-photography-of-condenser-microphone-270288/) | (Pexels) |
| subtitles-vs-dubbing-by-market | [photo 375885](https://www.pexels.com/photo/empty-cinema-with-white-screen-375885/) | Donald Tong |
| localization-vendor-brief-template | photo 3184465 | (Pexels) |
| ga4-export-website-metrics | photo 590022 | (Pexels) |
| what-is-mtpe-post-editing | photo 3631711 (打字机 "rewrite... edit...") | (Pexels) |
| international-website-legal-pages | photo 5668858 | (Pexels) |
| indesign-vs-framemaker-multilingual | photo 326501 (双屏设计工作站) | (Pexels) |

## 下载方式（无 API key 时）

1. WebSearch 搜 `pexels.com photo <主题词>`，从结果里的图片页 URL 提取数字 ID；
2. 用 CDN 地址直接裁剪下载：
   `https://images.pexels.com/photos/<ID>/pexels-photo-<ID>.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop`
3. 注意：部分 ID 已失效（返回 404 或 "Source is unreachable"），需多备 2–3 个候选逐个探测；
4. 验证：`file` 输出含 `JPEG ... 1200x630`，大小 ≤200KB，存入 `static/images/news/<slug>.jpg`。
