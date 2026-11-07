# Casa Luano concept website

An independent, six-page preview for Casa Luano by Wildflower. This is a static site ready for its own GitHub repository. Deploy the contents of `dist/` from any static host.

## Pages

- `index.html` — home and autoplaying pottery-session video
- `paint.html` — pottery painting
- `wheel.html` — wheel throwing, pricing and interactive wheel
- `menu.html` — selected food and drink menu
- `gather.html` — group visits and special occasions
- `visit.html` — story, location and second short film

## Develop

Requirements: Node.js 20 or newer, npm, and Python 3.10 or newer.

```bash
npm ci
npm run build
npm run preview
```

Open `http://localhost:8765`. Page copy and structure live in `build.py`; motion and interactions live in `src/site.js`; styles live in `src/styles.css`. `npm run build` writes the six HTML pages, bundles the pinned Lenis dependency, and minifies the site CSS and JavaScript. The optimized media in `dist/assets/` is committed with the site; `media-manifest.json` supplies image dimensions to the build.

The home film is a 23-second muted loop cut from the supplied pottery-session video. The full second film on the Visit page retains audio and user controls. Both files are H.264 MP4s with fast-start metadata.

The concept retains `noindex` until the café approves public use. Remove that meta tag in `build.py` when the official site is ready to be indexed.

The [optimization comparison](reports/comparison.md) includes the before and after Lighthouse results, asset sizes, and remaining deployment checks.

The supplied posts and menu are the source for prices, hours, and activity details. Confirm those details and the preferred booking contact with Casa Luano before using this as an official public website. The booking links in this concept lead to the public Instagram profile and do not send a message.
