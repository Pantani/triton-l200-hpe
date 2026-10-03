# Follow-up performance diagnosis

- Producer: independent SEO/performance reviewer.
- Consumer: parent implementation owner and final reviewer.
- State: read-only experiment complete; recommendation awaiting parent implementation.
- Snapshot: post-font candidate copied from `site/` to `/tmp/l200-perf-followup/`; no repository product assets or HTML modified by reviewer.
- Scope: user-authorized next performance cycle. No shared CUA session use; isolated shell Lighthouse only. The earlier final audit remains historical evidence, not current hosted acceptance.

## Publication blocker carried forward

E01 remains external-blocked until coordinator resolves it: parent reported the old `pantani.github.io/triton-l200-hpe/` URL changed to HTTP301 redirecting to `http://pantani.xyz/triton-l200-hpe/`, then DNS resolution failed. This evidence is coordinator-reported, not independently remeasured here. Earlier Search Console request predates this redirect and cannot establish current reachability/indexing. Local performance conclusions remain local.

## Actual LCP and bottleneck

Verified from `/tmp/l200-seo-fonts-mobile.json`: LCP is `.hero-img`, selected full-resolution WebP403,222 bytes, rendered412x852 CSS pixels. Its request is already high priority, eager and discoverable in the initial HTML. No LCP discovery failure is reported. Simulated LCP7,352ms contrasts with unthrottled observed52ms; do not conflate these measurement types.

CSS render-blocking savings are estimated870ms, but the same report estimates zero LCP savings from that insight. About1.2MB of additional gallery/split images enter the mobile navigation because native lazy-loading fetches nearby offscreen images. This is not evidence that lazy-loading attributes are absent. The full hero WebP saves only about12% against its458,624-byte JPEG because image detail/resolution were deliberately retained after the first reviewer caught visibly blurred480w output.

## Isolated experiments

Commands retain Lighthouse13.5.0 default mobile simulation, Chrome154, and no error reporting. Each temporary variant runs on `http://127.0.0.1:8776/<variant>/`; report paths below. One run per variant; results are diagnostic, not statistically robust field measures.

```sh
rtk proxy python3 -m http.server 8776 --bind 127.0.0.1 --directory /tmp/l200-perf-followup
rtk proxy npx --yes lighthouse http://127.0.0.1:8776/mobilecrop/ --quiet --chrome-flags=--headless --only-categories=performance --output=json --output-path=/tmp/l200-perf-mobilecrop.json --no-enable-error-reporting
```

| Variant | Performance | FCP ms | Simulated LCP ms | Transfer bytes |
| --- | ---: | ---: | ---: | ---: |
| Current baseline | 75 | 1653 | 7352 | 1727092 |
| Explicit hero preload | 76 | 1502 | 7352 | 1727213 |
| Inline both CSS files | 76 | 1352 | 7277 | 1726673 |
| Full hero quality72 | 76 | 1652 | 6752 | 1632272 |
| Mobile centered crop, quality82 | 79 | 1653 | 5627 | 1539333 |

Preload and CSS inlining do not materially fix LCP here; avoid adding them merely to satisfy a generic checklist. Quality72 preserves1453x1053 dimensions and saves94,820 bytes, but average pixel error rises from2.65 to3.71/255 and LCP improves only~0.6s. Encoding full-resolution AVIF at quality60 produced268,651 bytes, less effective than avoiding invisible mobile pixels while also introducing another format. It was not browser-benchmarked.

## Recommended minimal change

Generate `hero-front-mobile.webp` directly from the approved oriented hero JPEG, retaining the central800x1053 pixel rectangle and quality82/method6. The temporary file is215,360 bytes,46.6% smaller than full WebP while preserving vertical resolution and compression quality. Keep all original JPEGs and existing gallery candidates untouched.

Insert a mobile-only source **before** the existing full-WebP source:

```html
<source media="(max-width: 480px)" type="image/webp" srcset="assets/responsive/hero-front-mobile.webp">
```

The measured test used600px cutoff, so its412px result also applies to480px cutoff. Recommend the conservative480px cutoff until a wider viewport is visually verified. A centered horizontal crop preserves the currently visible pixels when cover remains height-limited: rendered hero height must be at least viewport width ×1053/800 (632px at480px viewport). The candidate hero content exceeds that on inspected phones; verify320/390/412/480 after implementation. At wider sizes retain the original full source to avoid altering composition. No CSS changes are required. Existing `width/height` on fallback remain original source dimensions; absolute-positioned hero dimensions are already established by CSS.

Measured crop variant: simulated LCP7.352→5.627s, performance75→79, transfer1.727→1.539MB. This is a concrete gain with no intentional loss of visible detail, but **does not meet a good mobile LCP threshold or establish field performance**. The parent should verify composition at target breakpoints and use exact candidate Lighthouse results for final claims. Additional gallery scheduling changes would introduce more complexity and need separate justification; do not silently bolt on JavaScript merely to improve a single lab score.

## Acceptance for parent implementation

- Deterministic generator creates crop from approved JPEG with EXIF orientation baked, zero metadata and no original mutation.
- Source is limited to narrow screens; full-resolution desktop and all17 gallery targets preserved.
- Test actual crop dimensions/pixel orientation and source reference, not only a copied string.
- Parent visual validation confirms same mobile crop/composition and no new blur; reviewer will independently run final tests and mobile/desktop Lighthouse on frozen candidate.
- E01 public URL/deployment and Google indexing remain separate acceptance gates.

Asset-only visual follow-up: reviewer used `view_image` to compare the temporary 800×1053 WebP with the approved JPEG. Sharpness, truck details and existing plate mask were retained without a new visible encoding artifact. This verifies the asset, not browser composition at every breakpoint. Reviewer-owned experimental server on port 8776 was stopped after measurements.

## Frozen implementation: independent acceptance

State: **pass for authorized publication**, with mobile lab residual explicit; this is not a claim of deployed parity or field performance.

Parent implemented the proposed centered crop and restricted it to `(max-width: 480px) and (orientation: portrait)`. Independent reviewer ran all 21 tests successfully in 0.093s. Generator rejects upscaling, bakes orientation, preserves source bytes and strips metadata. All 17 original JPEGs remain byte-identical to HEAD. Actual `hero-front-mobile.webp` is byte-identical to the temporary asset visually inspected above.

Frozen HTML SHA-256: `194ebb101d7167bd2205265435feb9108261aec93e2ae6900866e3ba8e2a52b1`. CSS SHA-256: `287fed467c09962e7acb378c3f71d553f4f43ca6212a69278e7b9400edf0e197`. Crop SHA-256: `f83e8c058512b79e0ef860a6462f6bff5fb3184b94c732f91d3849a672aee06d`.

Parent supplied browser verification (not repeated by reviewer to avoid shared-session interference): no overflow at 320/390/412/480/700/1440px; portrait hero heights 782/776/852/749px respectively at 320/390/412/480px, all above the image-fit preservation requirement; wider/landscape views retain the full source. Reviewer independently verified source media condition and exact asset bytes.

Fresh Lighthouse 13.5.0 against `http://localhost:8766/`, same mobile/desktop settings as prior runs. Parent owns this server; reviewer did not stop it. Files `/tmp/l200-seo-crop-final-mobile.json` and `/tmp/l200-seo-crop-final-desktop.json`.

| Device | Performance | Accessibility | Best practices | SEO checks | FCP ms | Simulated LCP ms | Transfer bytes | CLS |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| mobile | 79 | 100 | 100 | 100 | 1653 | 5627 | 1539326 | 0.00262 |
| desktop | 96 | 100 | 100 | 100 | 362 | 1362 | 1809548 | 0.0004 |

Mobile LCP improves 7.352→5.627s versus the previous final candidate, while preserving visible image detail; performance 75→79. This still is not a good mobile LCP lab result. Both runs use the intended hero source and have no failed accessibility/SEO checks. No new local blocker found. Parent reported root robots/sitemap deployment corrected and verified live; E01 domain/deployment/indexing acceptance remains coordinator-owned and must use fresh live evidence rather than this historical snapshot.

## Deployed mobile baseline — separate public environment

Producer: independent reviewer. State: **published navigation verified**, one public Lighthouse run completed. Coordinator reported deployment commit `14c91aa` and successful CI run `37103048725` with artifact byte parity; reviewer independently measured the published URL below, without repeating deployment mutation.

URL: `https://pantani.xyz/triton-l200-hpe/`. Lighthouse fetch time `2026-10-03T06:28:47.122Z` (03:28:47 America/Sao_Paulo). Requested and final displayed URLs match. Lighthouse 13.5.0 default mobile simulation, same category flags as local runs. Report: `/tmp/l200-seo-published-mobile.json`. No runtime error, run warning, or failed/non-200 network request was reported.

```sh
rtk proxy npx --yes lighthouse https://pantani.xyz/triton-l200-hpe/ --quiet --chrome-flags=--headless --only-categories=performance,accessibility,best-practices,seo --output=json --output-path=/tmp/l200-seo-published-mobile.json --no-enable-error-reporting
```

| Published mobile metric | Result |
| --- | ---: |
| Performance | 99 |
| Accessibility | 100 |
| Best practices | 100 |
| Automated SEO checks | 100 |
| Simulated FCP | 943 ms |
| Simulated LCP | 2,250 ms |
| TBT | 0 ms |
| CLS | 0.00262 |
| Transfer | 1,517,229 bytes |

The selected LCP element is the intended mobile hero crop, rendered 412×852 CSS pixels. Unthrottled observed LCP391ms is recorded separately from the simulated2,250ms result. This public navigation is a **new deployed baseline**, not a controlled before/after comparison with Python localhost; CDN delivery, protocol, caching and latency differ. Do not attribute the numerical gap from local5.627s to another source-code optimization.

This one public lab run is in the good LCP range, but does not establish field Core Web Vitals or search ranking. Remaining diagnostics estimate image savings845KiB and cache-lifetime savings1,354KiB; do not silently degrade the approved full-photo experience to maximize a score. Public URL reachability is now verified by this run, superseding E01's earlier DNS-failure snapshot for this exact URL at this time. Search Console sitemap processing and actual index inclusion remain coordinator-owned separate checks; no SEO-category score proves either.

Observed network protocols in this public run: h2.
