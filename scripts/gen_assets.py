"""Generate the animated SVG assets used by the profile README.

GitHub renders README images as static <img> tags, so every "dynamic" effect
here is CSS or SMIL animation baked into the SVG itself. No external fonts or
scripts are used, which keeps the files small and camo-proxy friendly.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SOCIAL = ROOT / "social"

SANS = "'Segoe UI',Inter,Arial,sans-serif"
MONO = "'JetBrains Mono',Consolas,'Courier New',monospace"
BG = "#08111f"
INK = "#e6edf3"
MUTED = "#8da2ba"
LINE = "#1d2d44"
CYAN = "#38bdf8"
VIOLET = "#a78bfa"
GREEN = "#34d399"
AMBER = "#fbbf24"


def svg(width: int, height: int, label: str, body: str, style: str = "") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{label}">'
        f"<style>{style}</style>{body}</svg>\n"
    )


def header(number: str, label: str) -> str:
    style = "@keyframes blink{50%{opacity:0}}.c{animation:blink 1.1s step-end infinite}"
    body = (
        f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{VIOLET}"/>'
        f'<stop offset=".5" stop-color="{CYAN}"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></linearGradient></defs>'
        f'<rect width="900" height="56" rx="10" fill="{BG}"/>'
        f'<rect x="18" y="16" width="42" height="24" rx="12" fill="{CYAN}" fill-opacity=".12" stroke="{CYAN}" stroke-opacity=".5"/>'
        f'<text x="39" y="33" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" fill="{CYAN}">{number}</text>'
        f'<text x="76" y="36" font-family="{SANS}" font-size="21" font-weight="700" letter-spacing="4" fill="{INK}">{label}</text>'
        f'<rect class="c" x="{84 + len(label) * 17}" y="20" width="10" height="20" fill="{CYAN}"/>'
        f'<path d="M0 55h900" stroke="{LINE}"/>'
        f'<rect x="0" y="53" width="420" height="3" rx="1.5" fill="url(#g)"/>'
    )
    return svg(900, 56, label, body, style)


def hero() -> str:
    roles = ["Data Engineer", "AI Product Builder", "Agent Systems Developer"]
    style = (
        "@keyframes role{0%{opacity:0;transform:translateY(8px)}4%,29%{opacity:1;transform:none}"
        "33%,100%{opacity:0;transform:translateY(-8px)}}"
        ".r{opacity:0;animation:role 9s infinite}"
        "@keyframes blink{50%{opacity:0}}.cur{animation:blink 1s step-end infinite}"
        "@keyframes float{0%,100%{transform:translate(0,0)}50%{transform:translate(-30px,20px)}}"
        ".o1{animation:float 9s ease-in-out infinite}.o2{animation:float 11s ease-in-out infinite reverse}"
        "@keyframes pulse{0%{transform:scale(1);opacity:.7}100%{transform:scale(2.6);opacity:0}}"
        ".p{transform-box:fill-box;transform-origin:center;animation:pulse 2s ease-out infinite}"
        "@keyframes flow{to{stroke-dashoffset:-40}}.e{stroke-dasharray:6 14;animation:flow 1.6s linear infinite}"
        "@keyframes glow{0%,100%{opacity:.35}50%{opacity:1}}.n{animation:glow 3s ease-in-out infinite}"
    )
    role_svg = "".join(
        f'<g class="r" style="animation-delay:{i * 3}s">'
        f'<text x="72" y="186" font-family="{MONO}" font-size="21" fill="{INK}">{r}</text>'
        f'<rect class="cur" x="{76 + len(r) * 12.6:.0f}" y="168" width="11" height="22" fill="{CYAN}"/></g>'
        for i, r in enumerate(roles)
    )
    nodes = [(640, 110), (735, 70), (820, 140), (700, 205), (805, 245), (610, 255)]
    edges = [(0, 1), (1, 2), (0, 3), (2, 3), (3, 4), (2, 4), (3, 5), (0, 5)]
    edge_svg = "".join(
        f'<path class="e" d="M{nodes[a][0]} {nodes[a][1]}L{nodes[b][0]} {nodes[b][1]}" '
        f'stroke="{CYAN if i % 2 else VIOLET}" stroke-width="1.6" style="animation-delay:-{i * .3:.1f}s"/>'
        for i, (a, b) in enumerate(edges)
    )
    node_svg = "".join(
        f'<circle class="p" cx="{x}" cy="{y}" r="6" fill="none" stroke="{CYAN}" style="animation-delay:{i * .35:.2f}s"/>'
        f'<circle class="n" cx="{x}" cy="{y}" r="6" fill="{CYAN if i % 2 else VIOLET}" style="animation-delay:{i * .5}s"/>'
        for i, (x, y) in enumerate(nodes)
    )
    body = (
        '<defs>'
        f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#050b16"/><stop offset="1" stop-color="#0c1830"/></linearGradient>'
        f'<linearGradient id="name" x1="0" x2="1"><stop offset="0" stop-color="{INK}"/><stop offset="1" stop-color="{CYAN}"/></linearGradient>'
        f'<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#12233a"/></pattern>'
        '<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="45"/></filter>'
        '<clipPath id="clip"><rect width="900" height="320" rx="16"/></clipPath>'
        '</defs>'
        '<g clip-path="url(#clip)">'
        '<rect width="900" height="320" fill="url(#bg)"/><rect width="900" height="320" fill="url(#grid)"/>'
        f'<circle class="o1" cx="740" cy="90" r="110" fill="{CYAN}" opacity=".28" filter="url(#blur)"/>'
        f'<circle class="o2" cx="820" cy="270" r="100" fill="{VIOLET}" opacity=".3" filter="url(#blur)"/>'
        f'{edge_svg}{node_svg}'
        '</g>'
        f'<rect x=".5" y=".5" width="899" height="319" rx="16" fill="none" stroke="{LINE}"/>'
        f'<text x="48" y="88" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{CYAN}">HELLO, I\'M</text>'
        f'<text x="46" y="140" font-family="{SANS}" font-size="46" font-weight="800" fill="url(#name)">Sanskar Chandawar</text>'
        f'<text x="48" y="186" font-family="{MONO}" font-size="21" fill="{CYAN}">&gt;_</text>{role_svg}'
        f'<text x="48" y="226" font-family="{SANS}" font-size="15" fill="{MUTED}">I build data platforms and AI products, from first input to useful interface.</text>'
        f'<rect x="48" y="248" width="318" height="32" rx="16" fill="#0f2238" stroke="#1e3a5a"/>'
        f'<circle class="p" cx="68" cy="264" r="5" fill="{GREEN}"/><circle cx="68" cy="264" r="5" fill="{GREEN}"/>'
        f'<text x="84" y="269" font-family="{MONO}" font-size="13" fill="{INK}">now building · FORGE// + CampusOps</text>'
    )
    return svg(900, 320, "Sanskar Chandawar, Data Engineer and AI Product Builder", body, style)


SKILLS = [
    ("AI PRODUCTS", "AI", VIOLET, ["RAG", "Agent workflows", "Hybrid search", "Grounded answers", "Prompt design", "LLM APIs"]),
    ("DATA ENGINEERING", "DB", CYAN, ["PySpark", "Databricks", "Delta Lake", "SQL", "Data quality", "Dimensional modeling"]),
    ("APPLICATION", "&lt;/&gt;", AMBER, ["Python", "FastAPI", "TypeScript", "React", "Next.js", "Tailwind CSS", "Framer Motion"]),
    ("DELIVERY", "CI", GREEN, ["PostgreSQL", "pgvector", "Docker", "GitHub Actions", "Power BI", "SQLite"]),
]


def skills() -> str:
    pw, ph, gap = 440, 162, 20
    style = (
        "@keyframes up{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}"
        ".chip{opacity:0;animation:up .5s ease-out forwards}"
        "@keyframes dot{0%,100%{opacity:.35}50%{opacity:1}}.dot{animation:dot 2.4s ease-in-out infinite}"
    )
    parts = []
    delay = 0.0
    for i, (title, glyph, color, items) in enumerate(SKILLS):
        x, y = (i % 2) * (pw + gap), (i // 2) * (ph + gap)
        parts.append(
            f'<linearGradient id="p{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{color}" stop-opacity=".14"/>'
            f'<stop offset=".6" stop-color="{BG}" stop-opacity="0"/></linearGradient>'
            f'<rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="14" fill="{BG}"/>'
            f'<rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="14" fill="url(#p{i})" stroke="{LINE}"/>'
            f'<rect x="{x + 20}" y="{y + 18}" width="36" height="36" rx="10" fill="{color}" fill-opacity=".15" stroke="{color}" stroke-opacity=".6"/>'
            f'<text x="{x + 38}" y="{y + 41}" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" fill="{color}">{glyph}</text>'
            f'<text x="{x + 68}" y="{y + 34}" font-family="{SANS}" font-size="15" font-weight="700" letter-spacing="2.5" fill="{INK}">{title}</text>'
            f'<text x="{x + 68}" y="{y + 52}" font-family="{MONO}" font-size="11" fill="{MUTED}">0{i + 1} · {len(items)} tools</text>'
            f'<path d="M{x + 20} {y + 68}h{pw - 40}" stroke="{LINE}"/>'
        )
        cx, cy = x + 20, y + 82
        for j, item in enumerate(items):
            w = round(len(item) * 7.2 + 34)
            if cx + w > x + pw - 20:
                cx, cy = x + 20, cy + 36
            parts.append(
                f'<g class="chip" style="animation-delay:{delay:.2f}s">'
                f'<rect x="{cx}" y="{cy}" width="{w}" height="28" rx="8" fill="#0f1b2d" stroke="{color}" stroke-opacity=".3"/>'
                f'<circle class="dot" cx="{cx + 13}" cy="{cy + 14}" r="3.5" fill="{color}" style="animation-delay:{j * .3:.1f}s"/>'
                f'<text x="{cx + 23}" y="{cy + 18.5}" font-family="{SANS}" font-size="13" fill="{INK}">{item}</text></g>'
            )
            cx += w + 8
            delay += 0.05
    return svg(pw * 2 + gap, ph * 2 + gap, "Skills: AI products, data engineering, application, delivery", "".join(parts), style)


def window(title: str, path: str) -> str:
    return (
        f'<rect width="720" height="360" rx="14" fill="{BG}"/><rect x=".5" y=".5" width="719" height="359" rx="14" fill="none" stroke="{LINE}"/>'
        f'<rect x="20" y="20" width="680" height="30" rx="7" fill="#0f1d31"/>'
        f'<circle cx="40" cy="35" r="5" fill="#fb7185"/><circle cx="58" cy="35" r="5" fill="{AMBER}"/><circle cx="76" cy="35" r="5" fill="#4ade80"/>'
        f'<text x="100" y="40" font-family="{MONO}" font-size="12" fill="{MUTED}">{path}</text>'
    )


def card_studio() -> str:
    stages = ["IDEA", "DESIGN", "BUILD", "SHIP"]
    style = (
        "@keyframes lit{0%,20%{fill-opacity:.9;stroke-opacity:1}30%,100%{fill-opacity:.12;stroke-opacity:.4}}"
        ".st{animation:lit 4s infinite}"
        "@keyframes flow{to{stroke-dashoffset:-24}}.ln{stroke-dasharray:4 8;animation:flow 1s linear infinite}"
        "@keyframes blink{50%{opacity:0}}.cur{animation:blink 1s step-end infinite}"
    )
    boxes = "".join(
        f'<rect class="st" x="{60 + i * 160}" y="190" width="120" height="54" rx="10" fill="{VIOLET}" stroke="{VIOLET}" style="animation-delay:{i}s"/>'
        f'<text x="{120 + i * 160}" y="223" text-anchor="middle" font-family="{MONO}" font-size="14" font-weight="700" fill="{INK}">{s}</text>'
        for i, s in enumerate(stages)
    )
    body = (
        '<defs><linearGradient id="t" x1="0" x2="1">'
        f'<stop offset="0" stop-color="{INK}"/><stop offset="1" stop-color="{VIOLET}"/></linearGradient></defs>'
        + window("FORGE//", "forge // studio.build")
        + f'<text x="40" y="108" font-family="{SANS}" font-size="36" font-weight="800" fill="url(#t)">FORGE//</text>'
        f'<rect class="cur" x="196" y="80" width="14" height="32" fill="{VIOLET}"/>'
        f'<text x="40" y="140" font-family="{MONO}" font-size="13" letter-spacing="2" fill="{VIOLET}">INDEPENDENT AI PRODUCT STUDIO</text>'
        f'<path class="ln" d="M60 217H660" stroke="{VIOLET}" stroke-width="2" stroke-opacity=".6"/>'
        + boxes
        + f'<circle r="6" fill="{INK}"><animateMotion dur="4s" repeatCount="indefinite" path="M120 270H600"/></circle>'
        f'<path d="M120 270H600" stroke="{LINE}" stroke-width="2"/>'
        f'<text x="40" y="320" font-family="{MONO}" font-size="12" fill="{MUTED}">software · automation · data products · MVPs</text>'
    )
    return svg(720, 360, "FORGE AI Product Studio", body, style)


def card_campus() -> str:
    style = (
        "@keyframes pulse{0%{transform:scale(1);opacity:.8}100%{transform:scale(2.4);opacity:0}}"
        ".p{transform-box:fill-box;transform-origin:center;animation:pulse 2s ease-out infinite}"
    )
    agent = (360, 220)
    sources = [("email", 160), ("timetable", 220), ("docs", 280)]
    channels = [("web", 160), ("telegram", 220), ("email", 280)]
    parts = [window("CampusOps", "campusops / agent_router")]
    parts.append(
        f'<text x="40" y="100" font-family="{SANS}" font-size="32" font-weight="800" fill="{INK}">CampusOps</text>'
        f'<text x="40" y="128" font-family="{MONO}" font-size="13" letter-spacing="2" fill="{GREEN}">RETRIEVE / COMPOSE / DELIVER</text>'
    )
    for i, (name, y) in enumerate(sources):
        d = f"M150 {y}C250 {y} 260 {agent[1]} {agent[0]} {agent[1]}"
        parts.append(
            f'<path d="{d}" fill="none" stroke="{LINE}" stroke-width="2"/>'
            f'<circle cx="150" cy="{y}" r="7" fill="{CYAN}"/>'
            f'<text x="138" y="{y + 5}" text-anchor="end" font-family="{MONO}" font-size="13" fill="{MUTED}">{name}</text>'
            f'<circle r="4" fill="{CYAN}"><animateMotion dur="2.4s" begin="{i * .8}s" repeatCount="indefinite" path="{d}"/></circle>'
        )
    for i, (name, y) in enumerate(channels):
        d = f"M{agent[0]} {agent[1]}C460 {agent[1]} 470 {y} 570 {y}"
        parts.append(
            f'<path d="{d}" fill="none" stroke="{LINE}" stroke-width="2"/>'
            f'<circle cx="570" cy="{y}" r="7" fill="{GREEN}"/>'
            f'<text x="584" y="{y + 5}" font-family="{MONO}" font-size="13" fill="{MUTED}">{name}</text>'
            f'<circle r="4" fill="{GREEN}"><animateMotion dur="2.4s" begin="{1.2 + i * .8}s" repeatCount="indefinite" path="{d}"/></circle>'
        )
    parts.append(
        f'<circle class="p" cx="{agent[0]}" cy="{agent[1]}" r="22" fill="none" stroke="{GREEN}" stroke-width="2"/>'
        f'<circle cx="{agent[0]}" cy="{agent[1]}" r="22" fill="#0f2a26" stroke="{GREEN}" stroke-width="2"/>'
        f'<text x="{agent[0]}" y="{agent[1] + 5}" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" fill="{GREEN}">AI</text>'
        f'<text x="40" y="330" font-family="{MONO}" font-size="12" fill="{MUTED}">email + timetable + docs -&gt; one useful daily brief</text>'
    )
    return svg(720, 360, "CampusOps academic AI agent", "".join(parts), style)


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    for filename, number, label in (
        ("h-projects.svg", "01", "PROJECTS"),
        ("h-stack.svg", "02", "SKILLS"),
        ("h-activity.svg", "03", "ACTIVITY"),
    ):
        (ASSETS / filename).write_text(header(number, label), encoding="utf-8")
    (ASSETS / "hero.svg").write_text(hero(), encoding="utf-8")
    (ASSETS / "skills.svg").write_text(skills(), encoding="utf-8")
    (SOCIAL / "card-ai-product-studio.svg").write_text(card_studio(), encoding="utf-8")
    (SOCIAL / "card-campusops.svg").write_text(card_campus(), encoding="utf-8")


if __name__ == "__main__":
    main()
