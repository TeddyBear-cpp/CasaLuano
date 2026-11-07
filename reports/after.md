# After optimization

Measured 7 November 2026 with the same Lighthouse 13.6.0, headless Chrome 156, local HTTP site, and simulated mobile settings used for the baseline. Each page was measured once; scores can vary between runs and do not represent visitor field data.

| Page | Mobile performance | Mobile LCP | Accessibility | Best practices | SEO |
| --- | ---: | ---: | ---: | ---: | ---: |
| Home | 91 | 3.00 s | 100 | 100 | 63 |
| Paint pottery | 91 | 3.06 s | 100 | 100 | 63 |
| Wheel workshops | 92 | 2.94 s | 100 | 100 | 63 |
| Food & drink | 95 | 2.50 s | 100 | 100 | 63 |
| Gather | 94 | 2.66 s | 100 | 100 | 63 |
| Visit | 93 | 2.69 s | 100 | 100 | 63 |

Desktop home: performance **93**, LCP **1.26 s**, accessibility **100**, best practices **100**, SEO **63**.

## Final inventory

| Item | Size |
| --- | ---: |
| Entire six-page static build | 5.59 MB |
| Two MP4 videos | 4.13 MB |
| Photos and logo | 1.33 MB |
| CSS, including Lenis styles | 32.7 KB |
| JavaScript, including bundled Lenis | 22.2 KB |

The build includes pinned Lenis 1.3.27, bundled locally through esbuild. Scroll smoothing applies to wheel input and section links; touch scrolling remains native. The site uses native scrolling when a visitor requests reduced motion. All 31 images have explicit dimensions, all local links resolve, and the checked pages logged no browser errors. The autoplaying home film remains muted with a pause control; it stops when off-screen.

The SEO score remains 63 because this independent concept deliberately blocks indexing. Remove `noindex` only when Casa Luano approves an official public launch. The three food snapshots are still only 130 pixels wide in the supplied material, so replacing those with higher-resolution photos is the main remaining visual improvement.
