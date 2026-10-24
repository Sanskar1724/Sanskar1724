"""Document the profile card assets.

The cards in this directory are hand-authored SVG summaries of real projects.
Repository social previews can be generated separately with GitHub's settings.
"""

from pathlib import Path


if __name__ == "__main__":
    cards = sorted(Path(__file__).resolve().parents[1].glob("social/card-*.svg"))
    print(f"{len(cards)} project cards available")
