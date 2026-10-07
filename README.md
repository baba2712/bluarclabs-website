# bluarclabs.com

Source for the Bluarc Labs company website: a static, single-page site hosted on GitHub Pages.

## Structure

| Path | Purpose |
|---|---|
| `index.html` | The page |
| `css/styles.css` | All styles (colours are tokens at the top of the file) |
| `js/main.js` | Mobile menu, header state, scroll reveal |
| `assets/` | Favicon, touch icon, social preview image |
| `404.html` | Not-found page |
| `CNAME` | Custom domain for GitHub Pages |

## Editing

No build step. Edit the files and push to `main`; GitHub Pages redeploys in about a minute.

To preview locally:

```
python -m http.server 8000
```

then open http://localhost:8000.

## Replacing the placeholder logo

The wordmark is an inline SVG plus text in `index.html` (header and footer) and `404.html`.
Swap those blocks and `assets/favicon.svg` for the final logo files.
