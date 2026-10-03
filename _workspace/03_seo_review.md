# Independent SEO re-audit

- Producer: independent performance/SEO reviewer
- Consumer: coordinator and technical owner
- Completion: local acceptance passed after two bounded repair rounds; external publication/indexing and lab performance residuals explicit
- Snapshot: base HEAD `7a07e4d` with SEO candidate; external cleanup changes preserved. HTML SHA-256 `9e8119f8565d7a06cfe8a3ccc51c9bc8b3339269e8c213292a5d913227509e3f`; CSS SHA-256 `287fed467c09962e7acb378c3f71d553f4f43ca6212a69278e7b9400edf0e197`.
- Environment: local Python preview; Lighthouse13.5.0, Chrome154, Node26.10, same configs as authoritative dark baseline. Public deployment is not established here.

## Independent checks

Ran `rtk proxy /tmp/l200-seo-venv/bin/python -m unittest discover -s tests -v`: **17 tests passed, 0.073s** after repairs and public-only gallery invariant. Reviewed JSON-LD, canonical, XML sitemap, source fact consistency, local asset references, owner attribution and public-file boundary. Product+Car and Offer price159900/BRL agree with visible content; qualified year/mileage are not misrepresented as exact dates/readings. Place wraps PostalAddress. No invented business, ratings, VIN, shipping or unsupported delivery claims.

Verified all17 approved JPEG source bytes equal `git show HEAD:<path>`. Full-size WebP dimensions match EXIF-oriented source dimensions; all have zero EXIF entries. Mean absolute pixel difference against oriented JPEG source is1.69–2.65 on0–255 scale (expected lossy recompression, not proof of semantic privacy by itself). Browser gallery visual inspection verified retained orientation/redactions and19/19 image instances loaded without failed assets.17 full-photo links remain. Small gallery previews retain full JPEG access.

Four generated SEO skills have required frontmatter names/descriptions and required sections; team-spec and existing phase artifacts resolve. Independent contract walkthrough: normal flow reaches frozen review; missing Search Console access becomes explicit external-pending; conflicting writers serialize; a spelling-only request remains direct; city-page pressure does not justify invented locality or trim. These are contract simulations, not induced runtime failures. Live external Git drift was actually handled by pausing/rebaselining. The first light-design baseline and its accessibility findings are superseded by external design, not fixes credited to this task.

## Findings and repair loop

| ID | Severity | Evidence | Action | Acceptance | State |
| --- | --- | --- | --- | --- | --- |
| R01 | Medium | Hero source480w chosen at390px even though object-fit cover stretches landscape photo across tall portrait hero; visible blur vs baseline. | Technical changed hero to full1453w WebP only; gallery stays responsive. | Browser selects full WebP at320/390 and screenshot regains sharpness. | resolved-local |
| R02 | Low | At320px enlarged H1 used287px height; main CTA began y840. Sticky header contact remained available. | Technical reduced narrow-screen title/padding; kept semantic location/year. | At320 CTA y677–733; at390 y669–725; no overflow. Smallest viewport still needs slight scroll for whole button, but label/contact remain available. | resolved-local |
| R03 | Low | External cleanup removed HEIC-dependent gallery test while dropping private source originals. | Coordinator added public-only invariant comparing gallery with approved JPEG set. | Independent17-test run passes with test_gallery_covers_all_approved_public_photos. | resolved-local |
| R04 | Medium | Fresh mobile Lighthouse FCP2.949s; render-blocking estimate2.150s. External Google Fonts CSS listed at835ms and local7KB CSS151ms. | Decide whether to self-host same font assets or retain current design's third-party loading as documented residual. Do not claim mobile performance fully solved. | Explicit measured disposition and, if changed, repeat final same-setting lab check. | resolved-local after second repair; residual lab bottlenecks documented |

## Lab comparison after R01/R02 repairs

Outputs: `/tmp/l200-seo-repaired-mobile.json` and `/tmp/l200-seo-repaired-desktop.json`. Baseline: `/tmp/l200-seo-dark-baseline-{mobile,desktop}.json`. Same commands as baseline; substitute output filename. Single-run simulated Lighthouse navigation, not field Core Web Vitals, ranking, or index evidence.

| Device | Before performance | After performance | Before LCP ms | After LCP ms | Before transfer bytes | After transfer bytes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| mobile | 70.0 | 70.0 | 10877.534 | 7652.175 | 5474811 | 1722747 |
| desktop | 91.0 | 94.0 | 1922.478 | 1522.768 | 5739891 | 1805107 |

Mobile transfer fell68.5%; desktop68.6%. Mobile performance score remains70, desktop91→94. Accessibility, best-practices and SEO automatic categories are100 on both. Mobile CLS0.00267, desktop0.000524; TBT0 on both. Unthrottled observed LCP216ms mobile/185ms desktop differs from simulated LCP and must not replace it selectively in reporting. Remaining image-delivery estimated savings (~1MB) are diagnostic opportunities; full hero resolution was deliberately retained after actual visible-quality regression.

## Rendering

Checked320,390,700,1440px widths: document scrollWidth equals viewport width, no horizontal overflow. Desktop1440 contact starts y769 and stays visible in1000px viewport; tablet700 contact y697. After narrow-screen repair,320/390 contact positions are above. Header WhatsApp remains accessible and image masking is visually retained. Full gallery and model-specific content were inspected. Browser stale-cache/debugger failure was recovered with a fresh tab/origin; no app content was modified by reviewer.

## Baseline ID reconciliation

- T01/C01/C02/C04: regional purchase intent in title/H1/description verified locally; exact HPE-S retained.
- T02: one-URL sitemap and canonical validated locally; public serving/submission after deployment remains external.
- T03: local schema/offer consistency verified. Coordinator owns actual Google Rich Results code-test evidence separately.
- T04/C05/DEPLOY-01: local correction does not establish published parity.
- T05: original no-access premise is superseded by coordinator's actual Search Console access. Read `_workspace/02_search_console.md` for observed index status and request acceptance; reviewer did not independently operate that account. Request acceptance is not inclusion.
- T06: invariant coverage present and independently passing.
- C03: factual capital/statewide visit content verified with no unsupported transport promise.
- PERF-01: materially reduced transfer; mobile lab bottleneck remains R04, not hidden.
- A11Y-01/A11Y-02: superseded by external redesign; final candidate accessibility100.
- UX-01: addressed through R02 and breakpoint checks.
- HOST-01: preview cache/compression warnings are not production defects; hosted baseline verified gzip and10-minute cache. Host behavior belongs outside project source.

## External acceptance

Publishing, live sitemap200/content parity, field performance, actual indexing and query ranking remain distinct from local acceptance. Google Rich Results code-test is separate from public URL validation; preserve optional-field warnings rather than fabricate reviews or availability. Coordinator's external evidence and final ledger are authoritative for actions outside this review's read-only scope.

## Final frozen candidate after R04

Technical owner self-hosted the same official font families and weights (8 WOFF2 files plus3 family licenses), preserving the redesign. A small Latin Barlow700 preload replaces the external Google Fonts dependency. Independent19-test run passed in0.078s, including local-font signature and license invariants. CUA rendering rechecked320/390/700/1440px with unchanged contact geometry and no horizontal overflow. Hero uses full WebP; final mobile/desktop screenshots confirm retained sharpness and typography.

Final artifact SHA-256:
- `site/index.html`: `4b2f04d22b3f613bbad2f0b8cde5a25cfda705e4d763038ceeca3362b14791d4`
- `site/styles.css`: `287fed467c09962e7acb378c3f71d553f4f43ca6212a69278e7b9400edf0e197`
- `site/fonts.css`: `610b9f3cdb0ed23a8427b5d646a115288279fe13e430fe76f0f4929a3a480e06`

Authoritative final lab outputs: `/tmp/l200-seo-fonts-mobile.json`, `/tmp/l200-seo-fonts-desktop.json`, same Lighthouse13.5.0 settings as dark baseline.

| Metric | Mobile before | Mobile final | Desktop before | Desktop final |
| --- | ---: | ---: | ---: | ---: |
| Performance | 70 | 75 | 91 | 96 |
| FCP ms | 2788.6 | 1653.1 | 776.7 | 362.3 |
| Simulated LCP ms | 10877.5 | 7352.0 | 1922.5 | 1361.5 |
| Transferred bytes | 5474811 | 1727092 | 5739891 | 1809452 |
| CLS | 0.03849 | 0.00262 | 0.00571 | 0.0004 |

Both devices retain100 accessibility/best-practices/SEO and0 TBT. Network logs show **zero external requests** in either final navigation. R04 removed the third-party blocking dependency and improved mobile FCP2.789s→1.653s and desktop0.777s→0.362s, while retaining the requested font design. Mobile total transfer fell68.5% and desktop68.5%.

The finite review loop is complete. **Residual, not hidden:** simulated mobile LCP is still7.352s and performance75, not an all-green mobile result; local render-blocking estimate is870ms and image-delivery diagnostic still finds theoretical savings. Further tuning should use deployed field data/representative throttled measurements rather than discarding vehicle-photo quality for a lab score. Full-resolution hero is intentional because480w visibly degraded the product. Local server lacks production compression/cache. No field-performance or ranking improvement is established by these runs.

Final screenshots outside the public repository:

- `/Users/pantani/.codex/visualizations/2026/10/03/01a0ffbb-2031-7060-856c-22a17b5c10d1/l200-seo-mobile-final.jpg`
- `/Users/pantani/.codex/visualizations/2026/10/03/01a0ffbb-2031-7060-856c-22a17b5c10d1/l200-seo-desktop-final.jpg`

Coordinator separately verified Google Rich Results code-test:1 valid Product snippet with optional aggregateRating/review/availability warnings; account evidence and result URL are in `_workspace/02_search_console.md`. The reviewer inspected the structured data and tests independently but did not repeat the coordinator's account or Google UI actions. Actual indexing request acceptance is not index inclusion.

Cleanup verified: reviewer-owned localhost servers on ports 8766, 8767 and 8768 stopped with exit 130 after SIGINT. Final review tab closed and viewport override reset.
