# bluarclabs.com

Source for the Bluarc Labs company website: a static, single-page site hosted on GitHub Pages.

## Structure

| Path | Purpose |
|---|---|
| `index.html` | The page, including SEO meta and JSON-LD structured data |
| `css/styles.css` | All styles; identity colours are tokens at the top of the file |
| `js/main.js` | Mobile menu, header state, scroll reveal |
| `assets/brand/` | Official identity SVGs (lockup, reverse lockup, symbol, SAFE endorsement). Use as supplied; do not redraw or recolour |
| `assets/fonts/` | Anek Latin (SIL OFL), web subset: Latin, weights 400–600, width 100 |
| `assets/icons/`, `favicon.ico`, `apple-touch-icon.png`, `site.webmanifest` | App and browser icons |
| `assets/og-image.png` | Social preview (identity social card, 1200 × 630) |
| `404.html` | Not-found page (self-contained) |
| `robots.txt`, `sitemap.xml`, `llms.txt`, `.well-known/security.txt` | Crawler and disclosure files |
| `CNAME` | Custom domain for GitHub Pages |

## Identity rules that affect the code

- Signature minimum 120px wide (site uses 144–160px). Symbol minimum 24px. SAFE endorsement minimum 167px.
- Text pairs: navy on ice/surface, slate on ice/surface, ocean on ice, ice on navy/ocean. Surf (`#78AEE0`) is for rules and artwork, never small text on light backgrounds.
- No glows, gradients, shields, radar/Wi-Fi arcs or network-node graphics. The enlarged symbol appears once (contact section), ocean on navy, edge-cropped.
- Fonts: Anek Latin 400, 500 and 600 only.

## Editing

No build step. Edit the files and push to `main`; GitHub Pages redeploys in about a minute.
When content changes, update `<lastmod>` in `sitemap.xml`. Renew `Expires` in `.well-known/security.txt` before 2027-10-08.

To preview locally:

```
python -m http.server 8000
```

then open http://localhost:8000.
