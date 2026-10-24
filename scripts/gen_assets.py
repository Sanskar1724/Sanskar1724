"""Generate the editorial SVG assets used by the profile README."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def header(number: str, label: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="64" viewBox="0 0 900 64" role="img" aria-label="{label}">
<style>text{{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}} .line{{animation:slide 4s ease-in-out infinite}} @keyframes slide{{from{{transform:translateX(-180px)}}to{{transform:translateX(900px)}}}} @media(prefers-reduced-motion:reduce){{*{{animation:none}}}}</style>
<text x="0" y="38" font-size="13" fill="#38bdf8">{number}</text>
<text x="40" y="38" font-family="Segoe UI,Arial,sans-serif" font-size="24" font-weight="700" letter-spacing="5" fill="#8b949e">{label}</text>
<rect y="54" width="900" height="1" fill="#30363d"/><rect class="line" y="53" width="180" height="3" fill="#38bdf8"/>
</svg>"""


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "h-projects.svg").write_text(header("01", "PROJECTS"), encoding="utf-8")
    (ASSETS / "h-stack.svg").write_text(header("02", "STACK"), encoding="utf-8")
    (ASSETS / "h-activity.svg").write_text(header("03", "ACTIVITY"), encoding="utf-8")


if __name__ == "__main__":
    main()
