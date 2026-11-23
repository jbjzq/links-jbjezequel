"""Render index.html from LINKS. Run: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
A = ROOT / "assets"

def icon(name):
    d = (A / f"{name}.path").read_text().strip()
    return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{d}"/></svg>'

# (label, sublabel, url, icon html, brand color)
SOCIAL = [
    ("YouTube", "@JBEvaboot · 7.1K subscribers", "https://www.youtube.com/@JBEvaboot?sub_confirmation=1", icon("youtube"), "#FF0000"),
    ("X", "@jb_jezequel", "https://x.com/jb_jezequel", icon("x"), "var(--ink)"),
    ("LinkedIn", "JB Jézéquel", "https://www.linkedin.com/in/jb-fullvision/", icon("linkedin"), "#0A66C2"),
    ("Instagram", "@jb_jezequel", "https://www.instagram.com/jb_jezequel/", icon("instagram"), "#E4405F"),
    ("TikTok", "@jb_jezequel", "https://www.tiktok.com/@jb_jezequel", icon("tiktok"), "var(--ink)"),
    ("Facebook", "JB Jézéquel", "https://www.facebook.com/profile.php?id=61586221183698", icon("facebook"), "#0866FF"),
    ("Substack", "jbjezequel.com · 1.6K subscribers", "https://www.jbjezequel.com/", icon("substack"), "#FF6719"),
]
COMPANIES = [
    ("Evaboot", "Export LinkedIn Sales Navigator leads", "https://evaboot.com/", '<img src="assets/evaboot.svg" alt="">', None),
    ("FullVision", "AI agents that grow your website and revenue.", "https://fullvision.io/", '<img src="assets/fullvision.png" alt="">', None),
]
HIDE = set()  # links waiting for a confirmed handle

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
html = html.replace("{{SOCIAL}}", section("Follow", SOCIAL)).replace("{{COMPANIES}}", section("My companies", COMPANIES))
(ROOT / "index.html").write_text(html)
print("index.html written")
