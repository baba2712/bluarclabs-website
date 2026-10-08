# bluarclabs.com

Source for the BluArc Labs company website: a static, multi-page site hosted on GitHub Pages.

## Structure

| Path | Purpose |
|---|---|
| `src/build.py` | Generates every page (shared head, SEO meta, JSON-LD, header, FAQ, footer) and `sitemap.xml`. Page metadata and FAQs live in its `PAGES` list |
| `src/pages/*.html` | Main content sections for each page |
| `src/og.py` | Regenerates per-page social cards in `assets/og/` (needs Pillow, fontTools and the BluArc Labs developer pack: `python src/og.py path/to/BluArc-Labs-Developer-Pack`) |
| `index.html`, `<page>/index.html` | Generated output. Do not edit by hand; edit `src/` and rebuild |
| `css/styles.css` | All styles; identity colours are tokens at the top of the file |
| `js/main.js` | Mobile menu, header state, scroll reveal |
| `assets/brand/` | Identity v1.0 artwork as supplied: `logo.svg` (horizontal, full colour), `symbol.svg`, `symbol-white.svg`, and the brand elements (`fluted-band-hero.svg` from the brand book's website example, `filament-fan.svg`, `seed-field.svg`, `link-lattice.svg`). Do not redraw, recolour or rebuild a lockup |
| `assets/fonts/` | BluArc Sans v1.0 (Regular, Medium, Bold), drawn for BluArc Labs; basic Latin only, so accents and most currency signs fall back to the system font |
| `assets/icons/`, `favicon.ico`, `apple-touch-icon.png`, `site.webmanifest` | App and browser icons |
| `assets/og/` | Per-page social previews built from the identity social card (1200 × 630) |
| `404.html` | Not-found page (self-contained) |
| `robots.txt`, `sitemap.xml`, `llms.txt`, `.well-known/security.txt` | Crawler and disclosure files |
| `CNAME` | Custom domain for GitHub Pages |

## Identity rules that affect the code

- Always write the name as **BluArc Labs** (capital B and A).
- Colours: Deep Sky `#1F8FD8`, white and Core Black `#0B0B0C` only. Tints (Deep Sky 50/25/10%) are for patterns, rules and panels, never text. They are still pending founder approval; if removed, replace `--sky-25` and `--sky-10` in `css/styles.css`.
- All text under 24px is Core Black, including links, labels and numbers. Deep Sky text only at 24px and above. On Deep Sky grounds, small text is Core Black; white only for large headlines.
- Buttons are Core Black pills with white labels.
- Logo minimum widths: horizontal 190px (site uses 190–196px), symbol 48px. Below 48px use the small symbol drawing (favicons already do).
- One brand element per surface: fluted band (home hero), filament fan (SAFE panels, company page), seed field (CTA band), link lattice (footer).
- Fonts: BluArc Sans 400, 500 and 700 only; no italic.

## Editing

Edit `src/`, then run `python src/build.py` (standard library only) and push to `main`; GitHub Pages redeploys in about a minute.
When content changes, update `LASTMOD` in `src/build.py` so the sitemap and structured data stay current. Renew `Expires` in `.well-known/security.txt` before 2027-10-08.

To preview locally:

```
python -m http.server 8000
```

then open http://localhost:8000.
