"""Generate the consistent section labels used by the profile README."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def header(number: str, label: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="64" viewBox="0 0 900 64" role="img" aria-label="{label}">
<rect width="900" height="64" rx="8" fill="#0b1424"/><text x="22" y="39" font-family="monospace" font-size="13" fill="#38bdf8">{number}</text><text x="64" y="39" font-family="Arial,sans-serif" font-size="23" font-weight="700" letter-spacing="4" fill="#e6edf3">{label}</text><path d="M0 57h900" stroke="#26364b"/><path d="M0 57h190" stroke="#38bdf8" stroke-width="3"/>
</svg>"""


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    for filename, number, label in (
        ("h-projects.svg", "01", "SELECTED PROJECTS"),
        ("h-stack.svg", "02", "TECHNICAL STACK"),
        ("h-writing.svg", "03", "TECHNICAL WRITING"),
        ("h-activity.svg", "04", "ACTIVITY"),
    ):
        (ASSETS / filename).write_text(header(number, label), encoding="utf-8")


if __name__ == "__main__":
    main()
