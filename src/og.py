"""Generate per-page social cards (1200 x 630) from the identity's social card.

Keeps the agency composition (signature, ocean-on-navy crop, reference label)
and replaces only the headline. Requires Pillow and the full Anek Latin TTF
from the developer identity pack:

    python src/og.py "path/to/social-card@2x.png" "path/to/AnekLatin[wdth,wght].ttf"
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "og"

ICE = (237, 244, 250)
NAVY = (18, 42, 69)

CARDS = {
    "ot-security": ["OT security for", "industrial plants."],
    "plant-analytics": ["Plant data into", "clearer decisions."],
    "embedded-sensing": ["Sensing built for", "real conditions."],
    "safe": ["Security for", "industrial computers."],
    "company": ["Built around", "the plant floor."],
    "contact": ["Let's talk about", "your plant."],
}


def main(card_path, font_path):
    OUT.mkdir(parents=True, exist_ok=True)
    base = Image.open(card_path).convert("RGB")  # 2400 x 1260
    s = base.width / 1200

    def save(img, name):
        small = img.resize((1200, 630), Image.LANCZOS)
        small.quantize(colors=64, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / f"{name}.png", optimize=True)

    save(base, "home")

    for name, lines in CARDS.items():
        img = base.copy()
        d = ImageDraw.Draw(img)
        # Clear the original headline area (left of the navy panel, between signature and label).
        d.rectangle([0, int(180 * s), int(838 * s), int(470 * s)], fill=ICE)
        size = 84
        while True:
            font = ImageFont.truetype(font_path, int(size * s))
            font.set_variation_by_axes([500, 100])  # axes: weight, width
            widest = max(d.textlength(l, font=font) for l in lines)
            if widest <= 720 * s or size <= 56:
                break
            size -= 2
        baselines = [297, 385] if size >= 76 else [290, 370]
        for line, base_y in zip(lines, baselines):
            d.text((60 * s, base_y * s), line, font=font, fill=NAVY, anchor="ls")
        save(img, name)
        print(name, size)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
