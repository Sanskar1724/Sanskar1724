"""Generate the animated SVG assets used by the profile README.

GitHub renders README images as static <img> tags, so every "dynamic" effect
here is CSS or SMIL animation baked into the SVG itself. No external fonts or
scripts are used, which keeps the files small and camo-proxy friendly.
"""

import random
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
PINK = "#f472b6"


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


def wallpaper() -> str:
    """Twilight landscape: a student on a hilltop with a glowing laptop."""
    rng = random.Random(1724)
    w, h = 1200, 480
    hill = "#0d0a1f"
    style = (
        "@keyframes tw{0%,100%{opacity:.25}50%{opacity:1}}"
        ".t1{animation:tw 3s ease-in-out infinite}.t2{animation:tw 4.5s ease-in-out infinite 1s}"
        ".t3{animation:tw 6s ease-in-out infinite 2s}"
        "@keyframes ss{0%{transform:translateX(-160px);opacity:0}2%{opacity:1}"
        "10%,100%{transform:translateX(520px);opacity:0}}.ss{animation:ss 8s linear infinite}"
        "@keyframes glow{0%,100%{opacity:.55}50%{opacity:.9}}.lg{animation:glow 3s ease-in-out infinite}"
        "@keyframes fly{0%,100%{transform:translate(0,0);opacity:.2}50%{transform:translate(8px,-14px);opacity:1}}"
        ".ff{animation:fly 5s ease-in-out infinite}"
        "@keyframes word{0%{opacity:0;transform:translateY(8px)}4%,29%{opacity:1;transform:none}"
        "33%,100%{opacity:0;transform:translateY(-8px)}}.w{opacity:0;animation:word 9s infinite}"
        "@keyframes blink{50%{opacity:0}}.cur{animation:blink 1s step-end infinite}"
    )
    stars = "".join(
        f'<circle class="t{rng.randint(1, 3)}" cx="{rng.uniform(0, w):.0f}" cy="{rng.uniform(0, 300) ** 1.1 / 1.8:.0f}" '
        f'r="{rng.uniform(.6, 1.7):.1f}" fill="#fff" style="animation-delay:{rng.uniform(0, 4):.1f}s"/>'
        for _ in range(120)
    )
    flies = "".join(
        f'<circle class="ff" cx="{rng.uniform(640, 1180):.0f}" cy="{rng.uniform(380, 460):.0f}" r="2.4" '
        f'fill="url(#fly)" style="animation-delay:{rng.uniform(0, 5):.1f}s;animation-duration:{rng.uniform(4, 7):.1f}s"/>'
        for _ in range(14)
    )
    doing = ["training small LLMs", "building AI agents", "shipping data pipelines"]
    words = "".join(
        f'<g class="w" style="animation-delay:{i * 3}s"><text x="96" y="300" font-family="{MONO}" font-size="19" fill="#bae6fd">{d}</text>'
        f'<rect class="cur" x="{100 + len(d) * 11.4:.0f}" y="284" width="10" height="20" fill="#7dd3fc"/></g>'
        for i, d in enumerate(doing)
    )
    person = (
        f'<g transform="translate(968 382) scale(1.9)" fill="{hill}">'
        '<circle class="lg" cx="10" cy="-22" r="30" fill="url(#lap)"/>'
        '<circle cx="-2" cy="-43" r="7.5"/>'
        '<path d="M-8 -34Q-13 -16 -10 0H8Q10 -17 5 -34Z"/>'
        '<path d="M-6 0L15 -12Q20 -14 22 -9L27 3H19L16 -4L2 4Z"/>'
        f'<path d="M1 -29Q7 -19 11 -14" stroke="{hill}" stroke-width="4" stroke-linecap="round" fill="none"/>'
        '<path d="M5 -12L10 -31L24 -29L19 -11Z" fill="#1b1838" stroke="#7dd3fc" stroke-opacity=".6" stroke-width=".8"/>'
        "</g>"
    )
    tree = (
        f'<g fill="{hill}"><rect x="1108" y="330" width="7" height="70"/>'
        '<circle cx="1111" cy="318" r="26"/><circle cx="1092" cy="334" r="18"/><circle cx="1130" cy="336" r="19"/></g>'
    )
    body = (
        "<defs>"
        '<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b0a2a"/>'
        '<stop offset=".45" stop-color="#2a1b5e"/><stop offset=".72" stop-color="#7b3f7a"/>'
        '<stop offset=".86" stop-color="#e0706a"/><stop offset="1" stop-color="#f6b26b"/></linearGradient>'
        '<radialGradient id="mglow"><stop offset="0" stop-color="#fef3c7" stop-opacity=".45"/><stop offset="1" stop-color="#fef3c7" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="lap"><stop offset="0" stop-color="#7dd3fc" stop-opacity=".9"/><stop offset="1" stop-color="#7dd3fc" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="fly"><stop offset="0" stop-color="#fef08a"/><stop offset="1" stop-color="#fef08a" stop-opacity="0"/></radialGradient>'
        '<linearGradient id="ssg" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>'
        '<linearGradient id="name" x1="0" x2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fbcfe8"/></linearGradient>'
        '<mask id="moon"><circle cx="1060" cy="105" r="36" fill="#fff"/><circle cx="1076" cy="94" r="32" fill="#000"/></mask>'
        f'<clipPath id="clip"><rect width="{w}" height="{h}" rx="18"/></clipPath>'
        "</defs>"
        '<g clip-path="url(#clip)">'
        f'<rect width="{w}" height="{h}" fill="url(#sky)"/>{stars}'
        '<circle cx="1060" cy="105" r="110" fill="url(#mglow)"/>'
        '<circle cx="1060" cy="105" r="36" fill="#fef3c7" mask="url(#moon)"/>'
        '<g transform="translate(260 40) rotate(22)"><rect class="ss" width="130" height="2" rx="1" fill="url(#ssg)"/></g>'
        '<g transform="translate(620 20) rotate(28)"><rect class="ss" width="110" height="2" rx="1" fill="url(#ssg)" style="animation-delay:4.5s"/></g>'
        '<path d="M0 360L90 300L170 330L260 272L360 320L450 282L560 330L660 266L760 316L860 286L960 322L1060 276L1200 322V480H0Z" fill="#3b2a63" opacity=".85"/>'
        '<path d="M0 402L120 352L220 382L330 332L440 386L560 352L690 396L800 362L930 402L1050 366L1200 392V480H0Z" fill="#22183f"/>'
        f'<path d="M0 480V448Q300 428 600 440Q820 446 900 404Q960 374 1040 382Q1130 392 1200 412V480Z" fill="{hill}"/>'
        f"{tree}{person}{flies}"
        "</g>"
        f'<text x="72" y="150" font-family="{MONO}" font-size="15" letter-spacing="4" fill="#fcd34d">HI, I\'M</text>'
        f'<text x="68" y="214" font-family="{SANS}" font-size="62" font-weight="800" fill="url(#name)">Sanskar Chandawar</text>'
        f'<text x="72" y="254" font-family="{SANS}" font-size="21" fill="#e9d5ff">Developer  ·  Computer Engineering Student  ·  Builder</text>'
        f'<text x="72" y="300" font-family="{MONO}" font-size="19" fill="#fcd34d">~</text>{words}'
    )
    return svg(w, h, "Sanskar Chandawar: a student coding on a hilltop under a starry twilight sky", body, style)


STATS = [
    ("35", "+", "Public repositories", "AI · data · full-stack", "&lt;/&gt;", "GITHUB", VIOLET),
    ("267", "+", "Automated tests", "across 3 featured projects", "&#10003;", "QUALITY", CYAN),
    ("11", "", "Datasets benchmarked", "public: finance · retail · fraud", "&#9638;", "RESEARCH", AMBER),
    ("1", "", "Research paper", "19-page preprint, MarginGraph", "PDF", "PUBLISHED", GREEN),
]


def stats() -> str:
    """Recruiter-facing impact tiles; each number rolls into place like an odometer."""
    tw, th, gap, row, dw = 210, 150, 20, 46, 25
    style = (
        "@keyframes up{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}"
        ".tile{opacity:0;animation:up .6s ease-out forwards}"
        "@keyframes roll{from{transform:translateY(0)}}"
        ".reel{animation:roll 1.8s cubic-bezier(.2,.8,.2,1) both}"
        "@keyframes pulse{0%{transform:scale(1);opacity:.8}100%{transform:scale(2.6);opacity:0}}"
        ".p{transform-box:fill-box;transform-origin:center;animation:pulse 2.2s ease-out infinite}"
    )
    parts = []
    for i, (value, suffix, label, sub, glyph, tag, color) in enumerate(STATS):
        x = i * (tw + gap)
        num_y = 98
        reels = []
        for j, ch in enumerate(value):
            stop = 10 + int(ch)
            digits = "".join(
                f'<tspan x="{x + 20 + j * dw}" y="{num_y + k * row}">{k % 10}</tspan>' for k in range(stop + 1)
            )
            reels.append(
                f'<text class="reel" style="transform:translateY(-{stop * row}px);animation-delay:{.2 + i * .15 + j * .12:.2f}s" '
                f'font-family="{SANS}" font-size="42" font-weight="800" fill="url(#n{i})">{digits}</text>'
            )
        parts.append(
            f'<linearGradient id="n{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="{color}"/></linearGradient>'
            f'<radialGradient id="g{i}" cx="1" cy="0" r="1"><stop offset="0" stop-color="{color}" stop-opacity=".22"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>'
            f'<clipPath id="c{i}"><rect x="{x}" y="{num_y - 40}" width="{tw}" height="{row - 2}"/></clipPath>'
            f'<clipPath id="t{i}"><rect x="{x}" y="0" width="{tw}" height="{th}" rx="16"/></clipPath>'
            f'<g class="tile" style="animation-delay:{i * .15:.2f}s">'
            f'<rect x="{x}" y="0" width="{tw}" height="{th}" rx="16" fill="{BG}"/>'
            f'<rect x="{x}" y="0" width="{tw}" height="{th}" rx="16" fill="url(#g{i})"/>'
            f'<g clip-path="url(#t{i})"><rect x="{x}" y="0" width="{tw}" height="4" fill="{color}"/></g>'
            f'<rect x="{x + .5}" y=".5" width="{tw - 1}" height="{th - 1}" rx="16" fill="none" stroke="{LINE}"/>'
            f'<rect x="{x + 18}" y="18" width="34" height="26" rx="8" fill="{color}" fill-opacity=".15" stroke="{color}" stroke-opacity=".55"/>'
            f'<text x="{x + 35}" y="36" text-anchor="middle" font-family="{MONO}" font-size="11" font-weight="700" fill="{color}">{glyph}</text>'
            f'<circle class="p" cx="{x + tw - 22}" cy="31" r="3.5" fill="{color}" style="animation-delay:{i * .5}s"/>'
            f'<circle cx="{x + tw - 22}" cy="31" r="3.5" fill="{color}"/>'
            f'<text x="{x + tw - 32}" y="35" text-anchor="end" font-family="{MONO}" font-size="10" letter-spacing="1.5" fill="{MUTED}">{tag}</text>'
            f'<g clip-path="url(#c{i})">{"".join(reels)}</g>'
            f'<text x="{x + 20 + len(value) * dw}" y="{num_y}" font-family="{SANS}" font-size="34" font-weight="800" fill="{color}">{suffix}</text>'
            f'<text x="{x + 20}" y="{num_y + 26}" font-family="{SANS}" font-size="14" font-weight="700" fill="{INK}">{label}</text>'
            f'<text x="{x + 20}" y="{num_y + 44}" font-family="{SANS}" font-size="12" fill="{MUTED}">{sub}</text>'
            "</g>"
        )
    return svg(4 * tw + 3 * gap, th, "35+ public repositories, 267+ automated tests, 11 public datasets benchmarked, 1 research paper", "".join(parts), style)


SKILLS = [
    # (title, glyph, color, core skills, working knowledge, proven in)
    ("AI &amp; LLMs", "AI", VIOLET, ["LLM evals", "RAG", "LLM APIs"],
     ["ReAct agents", "Fine-tuning", "QLoRA", "PyTorch", "Hugging Face"], "FinSight · CampusOps · PayTrust"),
    ("DATA ENGINEERING", "DB", CYAN, ["PySpark", "SQL", "Databricks"],
     ["Delta Lake", "Data warehousing", "Data quality"], "Retail Lakehouse · DataPilot"),
    ("SOFTWARE", "&lt;/&gt;", AMBER, ["Python", "FastAPI", "TypeScript"],
     ["React", "Next.js", "Java"], "FinSight · CampusOps"),
    ("ML &amp; DELIVERY", "ML", GREEN, ["scikit-learn", "LightGBM", "PostgreSQL"],
     ["Streamlit", "Docker", "GitHub Actions"], "MarginGraph · PayTrust"),
]


def chip_rows(items: list[tuple[str, bool]], width: int) -> list[list[tuple[str, bool, int]]]:
    rows: list[list[tuple[str, bool, int]]] = [[]]
    used = 0
    for item, core in items:
        w = round(len(item) * (7.6 if core else 7.2) + 34)
        if rows[-1] and used + w > width:
            rows.append([])
            used = 0
        rows[-1].append((item, core, w))
        used += w + 8
    return rows


def panel(i: int, x: int, y: int, pw: int, ph: int, title: str, glyph: str, sub: str, color: str) -> str:
    return (
        f'<linearGradient id="p{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{color}" stop-opacity=".16"/>'
        f'<stop offset=".6" stop-color="{BG}" stop-opacity="0"/></linearGradient>'
        f'<clipPath id="k{i}"><rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="14"/></clipPath>'
        f'<rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="14" fill="{BG}"/>'
        f'<rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="14" fill="url(#p{i})" stroke="{LINE}"/>'
        f'<g clip-path="url(#k{i})"><rect x="{x}" y="{y}" width="4" height="{ph}" fill="{color}"/></g>'
        f'<rect x="{x + 20}" y="{y + 18}" width="36" height="36" rx="10" fill="{color}" fill-opacity=".15" stroke="{color}" stroke-opacity=".6"/>'
        f'<text x="{x + 38}" y="{y + 41}" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" fill="{color}">{glyph}</text>'
        f'<text x="{x + 68}" y="{y + 34}" font-family="{SANS}" font-size="15" font-weight="700" letter-spacing="2.5" fill="{INK}">{title}</text>'
        f'<text x="{x + 68}" y="{y + 52}" font-family="{MONO}" font-size="11" fill="{MUTED}">{sub}</text>'
        f'<path d="M{x + 20} {y + 68}h{pw - 40}" stroke="{LINE}"/>'
    )


def skills() -> str:
    pw, gap, full, top = 440, 20, 900, 34
    style = (
        "@keyframes up{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}"
        ".chip{opacity:0;animation:up .5s ease-out forwards}"
        "@keyframes glow{0%,100%{fill-opacity:.16}50%{fill-opacity:.3}}.core{animation:glow 3s ease-in-out infinite}"
    )
    layouts = [chip_rows([(s, True) for s in core] + [(s, False) for s in rest], pw - 40)
               for _, _, _, core, rest, _ in SKILLS]
    ph = 82 + max(len(r) for r in layouts) * 36 + 40
    parts = [
        f'<rect x="0" y="4" width="26" height="18" rx="6" fill="{CYAN}" fill-opacity=".25" stroke="{CYAN}"/>'
        f'<text x="34" y="18" font-family="{SANS}" font-size="12.5" fill="{INK}">core strength</text>'
        f'<rect x="140" y="4" width="26" height="18" rx="6" fill="#0f1b2d" stroke="{CYAN}" stroke-opacity=".35"/>'
        f'<text x="174" y="18" font-family="{SANS}" font-size="12.5" fill="{MUTED}">working knowledge</text>'
        f'<text x="{full}" y="18" text-anchor="end" font-family="{MONO}" font-size="11" fill="{MUTED}">used in = projects behind each group</text>'
    ]
    delay = 0.0
    for i, ((title, glyph, color, core, rest, proof), rows) in enumerate(zip(SKILLS, layouts)):
        x, y = (i % 2) * (pw + gap), top + (i // 2) * (ph + gap)
        parts.append(panel(i, x, y, pw, ph, title, glyph, f"0{i + 1} · {len(core) + len(rest)} tools", color))
        for r, row in enumerate(rows):
            cx, cy = x + 20, y + 82 + r * 36
            for item, is_core, cw in row:
                if is_core:
                    chip = (
                        f'<rect class="core" x="{cx}" y="{cy}" width="{cw}" height="28" rx="8" fill="{color}" fill-opacity=".2" stroke="{color}"/>'
                        f'<text x="{cx + 12}" y="{cy + 18.5}" font-family="{SANS}" font-size="13" font-weight="700" fill="#fff">&#9733; {item}</text>'
                    )
                else:
                    chip = (
                        f'<rect x="{cx}" y="{cy}" width="{cw}" height="28" rx="8" fill="#0f1b2d" stroke="{color}" stroke-opacity=".3"/>'
                        f'<circle cx="{cx + 13}" cy="{cy + 14}" r="3" fill="{color}" fill-opacity=".7"/>'
                        f'<text x="{cx + 23}" y="{cy + 18.5}" font-family="{SANS}" font-size="13" fill="{INK}">{item}</text>'
                    )
                parts.append(f'<g class="chip" style="animation-delay:{delay:.2f}s">{chip}</g>')
                cx += cw + 8
                delay += 0.04
        parts.append(
            f'<path d="M{x + 20} {y + ph - 34}h{pw - 40}" stroke="{LINE}" stroke-dasharray="3 4"/>'
            f'<text x="{x + 20}" y="{y + ph - 14}" font-family="{MONO}" font-size="11" fill="{MUTED}">used in <tspan fill="{color}">{proof}</tspan></text>'
        )
    return svg(full, top + 2 * ph + gap, "Skills: LLM evals, RAG, LLM APIs, PySpark, SQL, Databricks, Python, FastAPI, TypeScript, scikit-learn, LightGBM and more", "".join(parts), style)


EXPLORING = [
    # (title, detail, category, color, tool)
    ("LLM from scratch", "RMSNorm · RoPE · GQA · SwiGLU", "LLM", VIOLET, "PyTorch"),
    ("LLM fine-tuning", "CPT → SFT → DPO → GRPO", "LLM", VIOLET, "Hugging Face"),
    ("Personal digital twin", "Qwen2.5 + QLoRA + Unsloth", "LLM", VIOLET, "Unsloth"),
    ("Recursive LM", "recursive sub-LLM calls", "LLM", VIOLET, "OpenRouter"),
    ("ReAct agent CLI", "think → act → observe", "AGENTS", CYAN, "Python"),
    ("AI agents from scratch", "tool calling + tracing", "AGENTS", CYAN, "Python"),
    ("Medallion lakehouse", "bronze → silver → gold", "DATA", AMBER, "Databricks"),
    ("Rural health assistant", "41 diseases, 98.4% accuracy", "ML", GREEN, "Streamlit"),
]


def explorations() -> str:
    cols, gap, full = 4, 12, 900
    tw, th = (full - gap * (cols - 1)) // cols, 124
    style = (
        "@keyframes up{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}"
        ".t{opacity:0;animation:up .55s ease-out forwards}"
        "@keyframes nudge{0%,100%{transform:translate(0,0)}50%{transform:translate(2px,-2px)}}"
        ".a{animation:nudge 2s ease-in-out infinite}"
    )
    parts = []
    for i, (name, detail, cat, color, tool) in enumerate(EXPLORING):
        x, y = (i % cols) * (tw + gap), (i // cols) * (th + gap)
        cw = len(cat) * 7 + 18
        tool_w = round(len(tool) * 6.6 + 18)
        parts.append(
            f'<g class="t" style="animation-delay:{i * .08:.2f}s">'
            f'<clipPath id="e{i}"><rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="14"/></clipPath>'
            f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="14" fill="{BG}" stroke="{LINE}"/>'
            f'<g clip-path="url(#e{i})"><rect x="{x}" y="{y}" width="{tw}" height="3" fill="{color}"/>'
            f'<circle cx="{x + tw}" cy="{y}" r="70" fill="{color}" fill-opacity=".08"/></g>'
            f'<text x="{x + 16}" y="{y + 30}" font-family="{MONO}" font-size="11" fill="{MUTED}">{i + 1:02d}</text>'
            f'<rect x="{x + 42}" y="{y + 17}" width="{cw}" height="18" rx="9" fill="{color}" fill-opacity=".15" stroke="{color}" stroke-opacity=".5"/>'
            f'<text x="{x + 42 + cw / 2:.1f}" y="{y + 30}" text-anchor="middle" font-family="{MONO}" font-size="10" font-weight="700" fill="{color}">{cat}</text>'
            f'<text class="a" x="{x + tw - 28}" y="{y + 32}" font-family="{SANS}" font-size="15" font-weight="700" fill="{color}">&#8599;</text>'
            f'<text x="{x + 16}" y="{y + 62}" font-family="{SANS}" font-size="14.5" font-weight="700" fill="{INK}">{name}</text>'
            f'<text x="{x + 16}" y="{y + 82}" font-family="{MONO}" font-size="11" fill="{MUTED}">{detail}</text>'
            f'<rect x="{x + 16}" y="{y + 94}" width="{tool_w}" height="20" rx="6" fill="#0f1b2d" stroke="{LINE}"/>'
            f'<text x="{x + 16 + tool_w / 2:.1f}" y="{y + 108}" text-anchor="middle" font-family="{MONO}" font-size="10.5" fill="{INK}">{tool}</text>'
            "</g>"
        )
    rows = -(-len(EXPLORING) // cols)
    return svg(full, rows * th + (rows - 1) * gap, "Recent explorations: LLM from scratch, fine-tuning, digital twin, recursive LM, agents, lakehouse, health ML", "".join(parts), style)


ROSE = "#fb7185"
ORANGE = "#fb923c"
PULSE = "@keyframes pulse{0%{transform:scale(1);opacity:.8}100%{transform:scale(2.4);opacity:0}}"
PULSE_STYLE = "transform-box:fill-box;transform-origin:center;animation:pulse 2s ease-out infinite"


def window(path: str, accent: str, badge: str = "") -> str:
    """Card frame: rotating gradient border, browser bar, optional LIVE/DEMO pill."""
    parts = [
        '<defs><linearGradient id="bd" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="720" y2="360">'
        f'<stop offset="0" stop-color="{accent}"/><stop offset=".5" stop-color="{accent}" stop-opacity="0"/>'
        f'<stop offset="1" stop-color="{CYAN}"/>'
        '<animateTransform attributeName="gradientTransform" type="rotate" from="0 360 180" to="360 360 180" dur="8s" repeatCount="indefinite"/>'
        "</linearGradient></defs>",
        f'<rect width="720" height="360" rx="14" fill="{BG}"/>',
        f'<rect x=".75" y=".75" width="718.5" height="358.5" rx="14" fill="none" stroke="{LINE}" stroke-width="1.5"/>',
        '<rect x=".75" y=".75" width="718.5" height="358.5" rx="14" fill="none" stroke="url(#bd)" stroke-width="1.5"/>',
        '<rect x="20" y="20" width="680" height="30" rx="7" fill="#0f1d31"/>',
        f'<circle cx="40" cy="35" r="5" fill="{ROSE}"/><circle cx="58" cy="35" r="5" fill="{AMBER}"/><circle cx="76" cy="35" r="5" fill="#4ade80"/>',
        f'<text x="100" y="40" font-family="{MONO}" font-size="12" fill="{MUTED}">{path}</text>',
    ]
    if badge:
        parts.append(
            f'<rect x="626" y="26" width="64" height="18" rx="9" fill="{GREEN}" fill-opacity=".12" stroke="{GREEN}" stroke-opacity=".5"/>'
            f'<circle cx="640" cy="35" r="3.5" fill="{GREEN}" style="{PULSE_STYLE}"/><circle cx="640" cy="35" r="3.5" fill="{GREEN}"/>'
            f'<text x="650" y="39" font-family="{MONO}" font-size="10" font-weight="700" fill="{GREEN}">{badge}</text>'
        )
    return "".join(parts)


def title(name: str, tagline: str, accent: str) -> str:
    return (
        f'<text x="40" y="98" font-family="{SANS}" font-size="32" font-weight="800" fill="{INK}">{name}</text>'
        f'<text x="40" y="124" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{accent}">{tagline}</text>'
    )


def metrics(items: list[str], accent: str) -> str:
    parts, x = [], 40
    for item in items:
        w = round(len(item) * 7 + 26)
        parts.append(
            f'<rect x="{x}" y="304" width="{w}" height="26" rx="13" fill="{accent}" fill-opacity=".12" stroke="{accent}" stroke-opacity=".5"/>'
            f'<text x="{x + w / 2:.1f}" y="321" text-anchor="middle" font-family="{MONO}" font-size="11.5" font-weight="700" fill="{INK}">{item}</text>'
        )
        x += w + 10
    return "".join(parts)


def card_finsight() -> str:
    style = (
        "@keyframes grow{0%,100%{transform:scaleY(.45)}50%{transform:scaleY(1)}}"
        ".b{transform-box:fill-box;transform-origin:bottom;animation:grow 4s ease-in-out infinite}"
        "@keyframes show{0%,8%{opacity:0;transform:translateY(6px)}18%,86%{opacity:1;transform:none}96%,100%{opacity:0}}"
        ".m{opacity:0;animation:show 7s ease-in-out infinite}"
        "@keyframes flow{to{stroke-dashoffset:-20}}.f{stroke-dasharray:5 5;animation:flow 1.2s linear infinite}"
    )
    heights = [60, 88, 52, 104, 76, 118]
    bars = "".join(
        f'<rect class="b" x="{48 + i * 36}" y="{282 - h}" width="22" height="{h}" rx="4" fill="{AMBER}" '
        f'fill-opacity="{.35 + i * .1:.2f}" style="animation-delay:{i * .25:.2f}s"/>'
        for i, h in enumerate(heights)
    )
    body = (
        window("finsight / grounded-assistant", AMBER)
        + title("FinSight AI", "MAKE EVERY RUPEE MAKE SENSE", AMBER)
        + f'<path d="M40 282H270" stroke="{LINE}"/>{bars}'
        f'<path class="f" d="M59 200L95 176L131 214L167 160L203 184L239 148L275 132" fill="none" stroke="{INK}" stroke-opacity=".7" stroke-width="1.6"/>'
        f'<g class="m"><rect x="390" y="150" width="290" height="34" rx="10" fill="#13233a"/>'
        f'<text x="406" y="172" font-family="{SANS}" font-size="13" fill="{INK}">Which budgets are at risk this month?</text></g>'
        f'<g class="m" style="animation-delay:.9s"><rect x="310" y="196" width="370" height="78" rx="10" fill="{AMBER}" fill-opacity=".08" stroke="{AMBER}" stroke-opacity=".45"/>'
        f'<text x="326" y="222" font-family="{SANS}" font-size="13" fill="{INK}">Food is at 92% of its limit with 9 days left.</text>'
        f'<rect x="326" y="238" width="132" height="22" rx="6" fill="#0f1b2d" stroke="{GREEN}" stroke-opacity=".5"/>'
        f'<text x="392" y="253" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{GREEN}">evidence: 14 rows</text>'
        f'<rect x="466" y="238" width="112" height="22" rx="6" fill="#0f1b2d" stroke="{CYAN}" stroke-opacity=".5"/>'
        f'<text x="522" y="253" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{CYAN}">source: ledger</text></g>'
        + metrics(["5 public benchmarks", "FinQA 48.7% → 71.0%", "77 tests + CI"], AMBER)
    )
    return svg(720, 360, "FinSight AI personal finance workspace", body, style)


def card_paytrust() -> str:
    style = (
        "@keyframes needle{0%,28%{transform:rotate(-62deg)}33%,61%{transform:rotate(0)}66%,95%{transform:rotate(62deg)}100%{transform:rotate(-62deg)}}"
        ".nd{transform-origin:170px 280px;animation:needle 6s ease-in-out infinite}"
        "@keyframes lit{0%,30%{fill-opacity:.85}36%,100%{fill-opacity:.08}}.pl{animation:lit 6s infinite}"
    )
    pills = "".join(
        f'<rect class="pl" x="330" y="{150 + i * 46}" width="150" height="34" rx="17" fill="{c}" fill-opacity=".08" stroke="{c}" style="animation-delay:{i * 2}s"/>'
        f'<text x="405" y="{172 + i * 46}" text-anchor="middle" font-family="{MONO}" font-size="13" font-weight="700" fill="{INK}">{label}</text>'
        f'<text x="496" y="{172 + i * 46}" font-family="{SANS}" font-size="12.5" fill="{MUTED}">{why}</text>'
        for i, (label, c, why) in enumerate([
            ("ALLOW", GREEN, "low risk, within policy"),
            ("ASK_USER", AMBER, "medium risk or approval gate"),
            ("DENY", ROSE, "policy violation or high risk"),
        ])
    )
    body = (
        '<defs><linearGradient id="gauge" gradientUnits="userSpaceOnUse" x1="90" x2="250">'
        f'<stop offset="0" stop-color="{GREEN}"/><stop offset=".5" stop-color="{AMBER}"/><stop offset="1" stop-color="{ROSE}"/></linearGradient></defs>'
        + window("paytrustai.streamlit.app", ROSE, "LIVE")
        + title("PayTrust AI", "SHOULD THIS AGENT BE ALLOWED TO PAY?", ROSE)
        + f'<path d="M90 280A80 80 0 0 1 250 280" fill="none" stroke="{LINE}" stroke-width="14" stroke-linecap="round"/>'
        '<path d="M90 280A80 80 0 0 1 250 280" fill="none" stroke="url(#gauge)" stroke-width="8" stroke-linecap="round"/>'
        f'<line class="nd" x1="170" y1="280" x2="170" y2="214" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
        f'<circle cx="170" cy="280" r="7" fill="{INK}"/>'
        f'<text x="170" y="178" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{MUTED}">risk score 0-100</text>'
        + pills
        + metrics(["IEEE-CIS 590k txns", "ROC-AUC 0.842", "128 tests"], ROSE)
    )
    return svg(720, 360, "PayTrust AI payment safety layer for AI agents", body, style)


def card_margin() -> str:
    style = (
        "@keyframes cas{0%,100%{fill-opacity:.15}20%{fill-opacity:.85}40%{fill-opacity:.15}}.st{animation:cas 4s infinite}"
        "@keyframes up{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}.up{animation:up 3s ease-in-out infinite}"
    )
    stages = [(260, "150 candidates"), (200, "LightGBM rerank"), (140, "MILP, margin &#8805; 15%"), (80, "2 add-ons")]
    bars = "".join(
        f'<rect class="st" x="40" y="{152 + i * 34}" width="{w}" height="24" rx="6" fill="{ORANGE}" stroke="{ORANGE}" stroke-opacity=".6" style="animation-delay:{i * .5}s"/>'
        f'<text x="{52 + w}" y="{169 + i * 34}" font-family="{MONO}" font-size="12" fill="{MUTED}">{label}</text>'
        for i, (w, label) in enumerate(stages)
    )
    body = (
        window("huggingface.co/spaces / MarginGraph", ORANGE, "DEMO")
        + title("MarginGraph", "A RANKER FOR RELEVANCE, AN OPTIMIZER FOR PROFIT", ORANGE)
        + bars
        + f'<g class="up"><text x="510" y="214" font-family="{SANS}" font-size="52" font-weight="800" fill="{ORANGE}">+24%</text>'
        f'<text x="512" y="240" font-family="{SANS}" font-size="13" fill="{MUTED}">add-on profit vs ranker</text>'
        f'<text x="512" y="258" font-family="{SANS}" font-size="11" fill="{MUTED}" fill-opacity=".7">(30-day replay, simulated cost)</text></g>'
        + metrics(["Hit@10 38.1%", "5 real datasets", "0 vs 164 floor breaks", "19-page paper"], ORANGE)
    )
    return svg(720, 360, "MarginGraph margin-aware recommendations", body, style)


def card_campus() -> str:
    style = PULSE + ".p{transform-box:fill-box;transform-origin:center;animation:pulse 2s ease-out infinite}"
    agent = (360, 205)
    sources = [("email", 150), ("timetable", 205), ("docs", 260)]
    channels = [("web", 150), ("telegram", 205), ("email", 260)]
    parts = [window("campus-ops-chi.vercel.app", GREEN, "LIVE"), title("CampusOps", "RETRIEVE / COMPOSE / DELIVER", GREEN)]
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
        + metrics(["62 tests", "hybrid search + OCR", "Vercel + Render"], GREEN)
    )
    return svg(720, 360, "CampusOps academic AI agent", "".join(parts), style)


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    for filename, number, label in (
        ("h-projects.svg", "01", "PROJECTS"),
        ("h-stack.svg", "02", "SKILLS"),
        ("h-explore.svg", "03", "EXPLORING"),
        ("h-activity.svg", "04", "ACTIVITY"),
    ):
        (ASSETS / filename).write_text(header(number, label), encoding="utf-8")
    (ASSETS / "wallpaper.svg").write_text(wallpaper(), encoding="utf-8")
    (ASSETS / "stats.svg").write_text(stats(), encoding="utf-8")
    (ASSETS / "skills.svg").write_text(skills(), encoding="utf-8")
    (ASSETS / "explorations.svg").write_text(explorations(), encoding="utf-8")
    for name, build in (
        ("finsight", card_finsight),
        ("paytrust", card_paytrust),
        ("margingraph", card_margin),
        ("campusops", card_campus),
    ):
        (SOCIAL / f"card-{name}.svg").write_text(build(), encoding="utf-8")


if __name__ == "__main__":
    main()
