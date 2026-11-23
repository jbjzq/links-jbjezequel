"""Render index.html from LINKS. Run: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
A = ROOT / "assets"

def icon(name):
    d = (A / f"{name}.path").read_text().strip()
    return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{d}"/></svg>'

# (label, sublabel, url, icon html, brand color)
SOCIAL = [
    ("YouTube", "@JBEvaboot", "https://www.youtube.com/@JBEvaboot", icon("youtube"), "#FF0000"),
    ("Instagram", "@jbjezequel", "https://www.instagram.com/jbjezequel/", icon("instagram"), "#E4405F"),
    ("TikTok", "@TIKTOK_HANDLE", "https://www.tiktok.com/@TIKTOK_HANDLE", icon("tiktok"), "var(--ink)"),
    ("LinkedIn", "JB Jézéquel", "https://www.linkedin.com/in/jb-jezequel-evaboot", icon("linkedin"), "#0A66C2"),
]
COMPANIES = [
    ("Evaboot", "Export LinkedIn Sales Navigator leads", "https://evaboot.com/", '<img src="assets/evaboot.svg" alt="">', None),
    ("FullVision", "Revenue attribution for B2B SaaS", "https://fullvision.io/", '<img src="assets/fullvision.png" alt="">', None),
]
HIDE = {"TikTok", "Instagram"}  # links waiting for a confirmed handle

def row(label, sub, url, ico, color):
    style = f' style="--brand:{color}"' if color else ""
    return f'''      <a class="link" href="{url}" target="_blank" rel="noopener"{style}>
        <span class="ico">{ico}</span>
        <span class="txt"><span class="label">{label}</span><span class="sub">{sub}</span></span>
        <svg class="arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>
      </a>'''

def section(title, items):
    rows = "\n".join(row(*i) for i in items if i[0] not in HIDE)
    return f'    <section>\n      <h2>{title}</h2>\n{rows}\n    </section>'

html = (ROOT / "template.html").read_text()
html = html.replace("{{SOCIAL}}", section("Follow", SOCIAL)).replace("{{COMPANIES}}", section("Build with me", COMPANIES))
(ROOT / "index.html").write_text(html)
print("index.html written")
