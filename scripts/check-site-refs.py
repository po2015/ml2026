#!/usr/bin/env python3
"""Verify that every internal reference in the built site resolves to a real file.

Scans public/**/*.html for src/href/srcset attributes and inline-style url()
references. Any root-relative URL (e.g. /images/foo.jpg, /services/) must map to
a file (or a directory containing index.html) under public/. Absolute URLs on the
site's own origin (baseURL) are checked the same way. External URLs, fragments,
mailto/tel/data: etc. are skipped.

Usage:  python3 scripts/check-site-refs.py [public-dir]
Exit 0 when clean, 1 listing every broken reference otherwise.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

SITE_ORIGIN = "https://www.medialocalize.com"
SKIP_SCHEMES = ("mailto:", "tel:", "data:", "javascript:", "sms:")
URL_RE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)")

CHECKED_ATTRS = ("src", "href")


class RefCollector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.refs = []  # (url, context)

    def handle_starttag(self, tag, attrs):
        line = self.getpos()[0]
        for name, value in attrs:
            if not value:
                continue
            if name in CHECKED_ATTRS:
                self.refs.append((value, f"{tag}[{name}] line {line}"))
            elif name == "srcset":
                for candidate in value.split(","):
                    url = candidate.strip().split()[0] if candidate.strip() else ""
                    if url:
                        self.refs.append((url, f"{tag}[srcset] line {line}"))
            elif name == "style":
                for match in URL_RE.finditer(value):
                    self.refs.append((match.group(2), f"{tag}[style url()] line {line}"))


def internal_path(url: str):
    """Return the root-relative path for an internal URL, or None to skip it."""
    url = url.strip()
    if not url or url.startswith("#") or url.startswith(SKIP_SCHEMES):
        return None
    if url.startswith(SITE_ORIGIN):
        url = url[len(SITE_ORIGIN):]
    elif url.startswith(("http://", "https://", "//")):
        return None  # external
    if not url.startswith("/"):
        return None  # relative URLs are not used for site assets/pages
    path = unquote(urlsplit(url).path)
    if not path or path == "/":
        return "/index.html"
    return path


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "public")
    if not root.is_dir():
        sys.exit(f"error: {root} not found — run `hugo` first")

    broken = []
    checked = 0
    for html_file in sorted(root.rglob("*.html")):
        collector = RefCollector()
        collector.feed(html_file.read_text(encoding="utf-8"))
        rel_page = html_file.relative_to(root)
        for url, context in collector.refs:
            path = internal_path(url)
            if path is None:
                continue
            checked += 1
            target = root / path.lstrip("/")
            if target.is_dir():
                target = target / "index.html"
            elif not target.suffix:
                target = target / "index.html"
            if not target.is_file():
                broken.append(f"{rel_page}: {context} -> {url}")

    print(f"checked {checked} internal references in {root}/")
    if broken:
        print(f"\n{len(broken)} broken reference(s):", file=sys.stderr)
        for line in broken:
            print(f"  {line}", file=sys.stderr)
        sys.exit(1)
    print("all internal references resolve")


if __name__ == "__main__":
    main()
