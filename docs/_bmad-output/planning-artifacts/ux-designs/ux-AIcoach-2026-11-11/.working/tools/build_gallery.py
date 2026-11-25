"""Assemble AIcoach concept folders into one gallery HTML (SVGs inlined).

Usage: python build_gallery.py <concepts_dir> <out.html> <template.html> [title] [intro_html]
"""
import html, json, re, sys
from pathlib import Path

ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2])
TPL = Path(sys.argv[3])
TITLE = sys.argv[4] if len(sys.argv) > 4 else "AIcoach Design Concepts"
INTRO = sys.argv[5] if len(sys.argv) > 5 else ""
PAGES = [
    ("01-landing.svg", "landing", "Landing"),
    ("02-upload.svg", "upload", "Upload"),
    ("03-upload-mobile.svg", "mobile", "Upload on phone"),
    ("04-result.svg", "result", "Result + AI coach"),
    ("05-other-pages.svg", "other", "Other pages"),
]


def md_to_html(md: str) -> str:
    out, para, in_list = [], [], False

    def inline(t):
        t = html.escape(t, quote=False)
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
        t = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", t)
        return t

    def flush():
        nonlocal para
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []

    for raw in md.splitlines():
        line = raw.rstrip()
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        b = re.match(r"^\s*(?:[-*]|\d+\.)\s+(.*)", line)
        if m:
            flush()
            if in_list:
                out.append("</ul>"); in_list = False
            if len(m.group(1)) == 1:
                continue
            out.append(f"<h4>{inline(m.group(2))}</h4>")
        elif b:
            flush()
            if not in_list:
                out.append("<ul>"); in_list = True
            out.append(f"<li>{inline(b.group(1))}</li>")
        elif not line.strip():
            flush()
            if in_list:
                out.append("</ul>"); in_list = False
        elif line.startswith("|"):
            flush()
            cells = [c.strip() for c in line.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            out.append('<div class="row">' + "".join(f"<span>{inline(c)}</span>" for c in cells) + "</div>")
        else:
            para.append(line.strip())
    flush()
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def clean_svg(text: str) -> str:
    text = re.sub(r"<\?xml[^>]*\?>", "", text)
    text = re.sub(r"<!DOCTYPE[^>]*>", "", text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)

    def root(m):
        tag = m.group(0)
        w = re.search(r'\swidth="([\d.]+)', tag)
        tag = re.sub(r'\s(width|height)="[^"]*"', "", tag, count=2)
        return tag[:-1] + f' data-w="{w.group(1) if w else 1440}" role="img">'

    return re.sub(r"<svg\b[^>]*>", root, text, count=1).strip()


concepts, fonts, problems = [], [], []
for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r"\d\d-", p.name)):
    meta = {}
    if (d / "concept.json").exists():
        try:
            meta = json.loads((d / "concept.json").read_text(encoding="utf-8"))
        except Exception as e:
            problems.append(f"{d.name}: concept.json {e}")
    nid = d.name[:2]
    meta.setdefault("name", d.name[3:].replace("-", " ").title())
    meta.setdefault("tagline", "")
    meta.setdefault("swatches", [])
    fonts += meta.get("fonts", [])
    md = (d / "concept.md").read_text(encoding="utf-8") if (d / "concept.md").exists() else ""
    pages = []
    for fn, key, label in PAGES:
        f = d / fn
        if f.exists():
            s = f.read_text(encoding="utf-8")
            if "<style" in s or "class=" in s:
                problems.append(f"{d.name}/{fn}: has <style> or class")
            pages.append((key, label, clean_svg(s)))
        else:
            problems.append(f"{d.name}/{fn}: missing")
    concepts.append((nid, meta, md_to_html(md), pages))

fam = {}
for f in fonts:
    name, _, axes = f.partition(":")
    if name.strip():
        fam.setdefault(name.strip(), set())
        if axes:
            fam[name.strip()].add(axes)
fam.setdefault("Geist", {"wght@400;500;600"})
fam.setdefault("Geist Mono", {"wght@400;500"})
parts = []
for name, axes in fam.items():
    q = "family=" + name.replace(" ", "+")
    if axes:
        q += ":" + sorted(axes, key=len)[-1]
    parts.append(q)
font_link = "https://fonts.googleapis.com/css2?" + "&amp;".join(parts) + "&amp;display=swap"

nav, sections = [], []
for nid, meta, rationale, pages in concepts:
    sw = "".join(f'<i style="background:{html.escape(c)}" title="{html.escape(c)}"></i>' for c in meta["swatches"][:6])
    nav.append(f'<a class="chip" href="#c{nid}" data-c="{nid}"><b>{nid}</b><span>{html.escape(meta["name"])}</span><span class="sw">{sw}</span></a>')
    figs = "".join(
        f'<figure class="shot" data-c="{nid}" data-p="{key}">'
        f'<figcaption><span class="pl">{label}</span><span class="cn">{nid} {html.escape(meta["name"])}</span>'
        f'<button type="button" class="zoom" aria-pressed="false">Actual size</button></figcaption>'
        f'<div class="frame">{svg}</div></figure>' for key, label, svg in pages)
    sections.append(
        f'<section class="concept" id="c{nid}" data-c="{nid}">'
        f'<header class="ch"><div class="num">{nid}</div><div><h2>{html.escape(meta["name"])}</h2>'
        f'<p class="tag">{html.escape(meta["tagline"])}</p><div class="sw big">{sw}</div></div></header>'
        f'<details class="why" open><summary>Concept notes</summary><div class="md">{rationale}</div></details>'
        f'<div class="shots">{figs}</div></section>')

page_tabs = "".join(f'<button type="button" class="ptab" data-p="{k}">{l}</button>' for _, k, l in PAGES)
out = (TPL.read_text(encoding="utf-8")
       .replace("{{TITLE}}", html.escape(TITLE))
       .replace("{{INTRO}}", INTRO)
       .replace("{{FONTLINK}}", font_link)
       .replace("{{NAV}}", "".join(nav))
       .replace("{{PAGETABS}}", page_tabs)
       .replace("{{SECTIONS}}", "".join(sections))
       .replace("{{COUNT}}", str(len(concepts))))
OUT.write_text(out, encoding="utf-8")
ids = re.findall(r'\sid="([^"]+)"', out)
from collections import Counter
dups = sorted(i for i, n in Counter(ids).items() if n > 1)
print(f"wrote {OUT} ({OUT.stat().st_size/1e6:.2f} MB), concepts={len(concepts)}, duplicate ids={dups[:10]}")
for p in problems:
    print("WARN", p)
