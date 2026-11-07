# Before optimization

Baseline captured 7 November 2026, before adding Lenis or changing the site media. Measurements used Lighthouse 13.6.0 in headless Chrome 156 against the local HTTP site. Mobile results use Lighthouse's simulated mobile throttling. Each page was measured once in the comparable six-page batch; the desktop home page was measured once. These are lab results, not visitor field data.

| Page | Mobile performance | Mobile LCP | Accessibility | Best practices | SEO |
| --- | ---: | ---: | ---: | ---: | ---: |
| Home | 64 | 6.03 s | 100 | 100 | 63 |
| Paint pottery | 76 | 5.88 s | 100 | 100 | 63 |
| Wheel workshops | 79 | 4.92 s | 100 | 100 | 63 |
| Food & drink | 83 | 4.23 s | 100 | 100 | 63 |
| Gather | 80 | 4.74 s | 100 | 100 | 63 |
| Visit | 73 | 7.37 s | 100 | 100 | 63 |

Desktop home: performance **89**, LCP **1.80 s**, accessibility **100**, best practices **100**, SEO **63**.

## Baseline inventory

| Item | Size |
| --- | ---: |
| Entire six-page static build | 20.44 MB |
| Two MP4 videos | 15.24 MB |
| Photos and logo | 5.09 MB |
| CSS | 36.8 KB |
| Site JavaScript | 5.9 KB |

Findings: both original videos were larger than needed for their display size; several photos were much larger than rendered; all 31 `<img>` instances lacked explicit dimensions; initial hero content used an opacity reveal that delayed the largest contentful paint; section links used CSS smooth scrolling, while wheel and trackpad movement remained native. Internal links had no broken targets. The SEO score reflected the intentional `noindex` setting on this concept preview.
