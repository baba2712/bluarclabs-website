"""Generate per-page social cards (1200 x 630) on the BluArc Labs identity.

White ground with the horizontal full-colour logo and the headline in BluArc
Sans Bold (last line in Deep Sky), beside a Deep Sky panel carrying the whole
white symbol. Needs Pillow, fontTools and the developer pack:

    python src/og.py "path/to/BluArc-Labs-Developer-Pack"
"""

import sys
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "og"

WHITE = (255, 255, 255)
SKY = (31, 143, 216)
BLACK = (11, 11, 12)

CARDS = {
    "home": ["Real conditions.", "Clearer decisions."],
    "ot-security": ["OT security for", "industrial plants."],
    "plant-analytics": ["Plant data into", "clearer decisions."],
    "embedded-sensing": ["Sensing built for", "real conditions."],
    "safe": ["Security for", "industrial computers."],
    "company": ["Built around", "the plant floor."],
    "contact": ["Let's talk about", "your plant."],
}

S = 2  # draw at 2x, then downsample
W, H = 1200 * S, 630 * S
PANEL_X = 820 * S


def kerning(path):
    """Pair kerning from the font's GPOS (Pillow's basic layout ignores it)."""
    font = TTFont(path)
    cmap = font.getBestCmap()
    by_glyph = {g: chr(c) for c, g in cmap.items()}
    pairs = {}
    for lookup in font["GPOS"].table.LookupList.Lookup:
        if lookup.LookupType != 2:
            continue
        for st in lookup.SubTable:
            if st.Format != 1:
                continue
            for first, pset in zip(st.Coverage.glyphs, st.PairSet):
                for rec in pset.PairValueRecord:
                    a, b = by_glyph.get(first), by_glyph.get(rec.SecondGlyph)
                    if a and b and rec.Value1 is not None:
                        pairs[a + b] = getattr(rec.Value1, "XAdvance", 0) or 0
    return pairs, font["head"].unitsPerEm


def draw_text(d, xy, text, font, fill, kern, upm, tracking=0.0):
    x, y = xy
    size = font.size
    for i, ch in enumerate(text):
        d.text((x, y), ch, font=font, fill=fill, anchor="ls")
        x += d.textlength(ch, font=font) + tracking * size
        if i + 1 < len(text):
            x += kern.get(ch + text[i + 1], 0) * size / upm


def text_width(d, text, font, kern, upm):
    w = sum(d.textlength(ch, font=font) for ch in text)
    return w + sum(kern.get(text[i:i + 2], 0) for i in range(len(text) - 1)) * font.size / upm


def main(pack):
    pack = Path(pack)
    logo = Image.open(pack / "logos/png/bluarc-labs-horizontal-full-colour-2400w.png").convert("RGBA")
    symbol = Image.open(pack / "logos/png/bluarc-labs-symbol-white-1024w.png").convert("RGBA")
    bold = pack / "fonts/otf/BluArcSans-Bold.otf"
    medium = pack / "fonts/otf/BluArcSans-Medium.otf"

    logo_w = 300 * S
    logo = logo.resize((logo_w, round(logo.height * logo_w / logo.width)), Image.LANCZOS)
    sym_w = 260 * S
    symbol = symbol.resize((sym_w, round(symbol.height * sym_w / symbol.width)), Image.LANCZOS)
    label_font = ImageFont.truetype(str(medium), 20 * S)
    kern_b, upm = kerning(bold)
    kern_m, _ = kerning(medium)

    OUT.mkdir(parents=True, exist_ok=True)
    for name, lines in CARDS.items():
        img = Image.new("RGB", (W, H), WHITE)
        d = ImageDraw.Draw(img)
        d.rectangle([PANEL_X, 0, W, H], fill=SKY)
        img.paste(symbol, (PANEL_X + (W - PANEL_X - symbol.width) // 2, (H - symbol.height) // 2), symbol)
        img.paste(logo, (64 * S, 64 * S), logo)

        size = 76
        while True:
            font = ImageFont.truetype(str(bold), size * S)
            if max(text_width(d, l, font, kern_b, upm) for l in lines) <= 690 * S or size <= 52:
                break
            size -= 2
        lh = round(size * 1.08)
        base = 360
        for i, line in enumerate(lines):
            draw_text(d, (64 * S, (base + i * lh) * S), line, font, SKY if i == len(lines) - 1 else BLACK, kern_b, upm, -0.015)

        draw_text(d, (64 * S, 566 * S), "INDUSTRIAL TECHNOLOGY · INDIA", label_font, BLACK, kern_m, upm, 0.08)

        small = img.resize((1200, 630), Image.LANCZOS)
        small.quantize(colors=64, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / f"{name}.png", optimize=True)
        print(name, size)


if __name__ == "__main__":
    main(sys.argv[1])
