# Optimization comparison

Casa Luano concept site · 7 November 2026

| Measure | Before | After | Change |
| --- | ---: | ---: | ---: |
| Six-page build size | 20.44 MB | 5.59 MB | **72.7% smaller** |
| Photos and logo | 5.09 MB | 1.33 MB | **73.8% smaller** |
| Videos | 15.24 MB | 4.13 MB | **72.9% smaller** |
| Average mobile Lighthouse performance | 76 | 93 | **+17 points** |
| Average mobile LCP | 5.53 s | 2.81 s | **49% faster** |
| Images with explicit dimensions | 0 of 31 | 31 of 31 | **All images** |
| Broken internal links | 0 | 0 | No regression |

| Page | Performance before → after | LCP before → after |
| --- | ---: | ---: |
| Home | 64 → 91 | 6.03 → 3.00 s |
| Paint pottery | 76 → 91 | 5.88 → 3.06 s |
| Wheel workshops | 79 → 92 | 4.92 → 2.94 s |
| Food & drink | 83 → 95 | 4.23 → 2.50 s |
| Gather | 80 → 94 | 4.74 → 2.66 s |
| Visit | 73 → 93 | 7.37 → 2.69 s |

The desktop home page moved from **89 to 93** for performance and from **1.80 to 1.26 seconds** for LCP. Accessibility and best-practices scores stayed at **100** on every measured page.

## What changed

- Added [Lenis 1.3.27](https://github.com/darkroomengineering/lenis/blob/main/README.md) for smooth wheel and anchor scrolling. The library is bundled in the site JavaScript; touch scrolling stays native, and reduced-motion settings disable smoothing.
- Converted 11 large JPEGs to resized WebP files and reduced the logo to its display scale.
- Cut the autoplay home footage to a focused 23-second loop, removed its unused audio, and encoded it at 480 × 854. The Visit page film keeps its full length and audio at 540 × 960. Both H.264 files use fast-start metadata.
- Removed opacity reveals from above-the-fold hero content while keeping scroll reveals deeper in the pages.
- Added image dimensions to the generated HTML, minified CSS and JavaScript, and kept the static output self-contained for a separate GitHub repository.

## Method and limits

Lighthouse 13.6.0 ran in headless Chrome 156 against `http://127.0.0.1:8765/` on 7 November 2026. Six mobile pages and the desktop home page were measured once before and once after, with identical settings. Mobile scores use Lighthouse simulated throttling. Lab scores vary with machine load and are not Core Web Vitals field measurements. See [the baseline](before.md) and [the final audit](after.md) for page scores.

The local Python server does not model a production host's Brotli compression, CDN caching, or edge latency. Those need a follow-up check after the GitHub-based deployment target is chosen.

The concept intentionally includes `noindex`, so Lighthouse SEO stayed at **63**. The site should remain unindexed until the café approves public use. Prices, hours, and preferred booking details still need confirmation, and the three supplied food photos remain low resolution.

After this audit, a 0.20 MB JPEG and static Open Graph metadata were added for messaging previews. The current build is 5.80 MB. The Lighthouse results above describe the audited build; the sharing metadata was not separately remeasured.
