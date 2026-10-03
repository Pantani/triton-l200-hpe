# Performance and visual baseline

Producer: performance specialist. Consumer: SEO orchestrator and final reviewer.
State: baseline complete; final implementation re-audit pending. The authoritative comparison baseline is the dark design in the last section; the earlier light baseline is preserved as superseded evidence.
Date: 2026-10-03 (America/Sao_Paulo).

## Scope and evidence

Verified repository: static HTML/CSS in `site/`; no frontend build or JavaScript. README requires retaining 17 photo derivatives, preserving redactions, and excluding original photos and private documents from Pages. Only `site/` is deployed.

Verified local baseline HTML SHA-256: `3218d1b20465a2c23e56b1db961101bfb5e27d371edd79ba063991d04d0d3850`.
Live HTTP 200 HTML SHA-256: `21d16a0b6e87a30cb2cba2402267afb7357da0d5afce238a752d17ee6c98d7e9`.
Source: direct HTTPS retrieval of https://pantani.github.io/triton-l200-hpe/ saved to `/tmp/l200-seo-production-baseline.html`.
The live page has the earlier design with Google Fonts; local HTML uses system fonts and substantially different layout. Local findings are not proof of deployed behavior.

## Reproduction

Runtime: Python 3.14.8; Node v26.10.0; Lighthouse 13.5.0; HeadlessChrome 154.0.0.0. Lighthouse flags verified using `--help`.

```sh
rtk proxy python3 -m http.server 8766 --bind 127.0.0.1 --directory site
rtk proxy npx --yes lighthouse http://127.0.0.1:8766/ --quiet --chrome-flags=--headless --only-categories=performance,accessibility,best-practices,seo --output=json --output-path=/tmp/l200-seo-baseline-mobile.json --no-enable-error-reporting
rtk proxy npx --yes lighthouse http://127.0.0.1:8766/ --quiet --chrome-flags=--headless --preset=desktop --only-categories=performance,accessibility,best-practices,seo --output=json --output-path=/tmp/l200-seo-baseline-desktop.json --no-enable-error-reporting
```

These are single-run laboratory navigation measurements, not field Core Web Vitals, ranking, conversion, or Search Console evidence. Mobile uses Lighthouse simulated throttling (150ms RTT, 1638.4 Kbps, 4x CPU), 412x823 CSS pixels, DPR 1.75. Simulator LCP differs substantially from unthrottled observed LCP and must not be presented as observed user latency.

| Metric | Mobile | Desktop |
| --- | ---: | ---: |
| Performance | 75 | 97 |
| Accessibility | 95 | 95 |
| Best practices | 100 | 100 |
| SEO automated checks | 100 | 100 |
| Simulated FCP | 751 ms | 202 ms |
| Simulated LCP | 9,076 ms | 1,222 ms |
| Observed unthrottled LCP | 603 ms | 46 ms |
| TBT | 0 ms | 0 ms |
| CLS | 0 | 0 |
| Initial measured transfer | 2,739,095 bytes | 1,906,018 bytes |

## Findings

### PERF-01: oversized image transfer — verified, implement and remeasure

Hero JPEG is 458,624 bytes. Lighthouse desktop image-delivery insight estimates 1,567,892 bytes savings among the initial images. Original JPEGs are used for small gallery cells without responsive candidates. Seven exterior JPEG assets contributed to the mobile navigation network payload despite gallery lazy loading. The browser determines the lazy-load proximity threshold, so lazy loading alone does not imply zero early gallery transfer.

Recommendation: generate smaller responsive derivatives from existing sanitized JPEGs, preserve full JPEG links, retain alt text and explicit dimensions, normalize orientation correctly, and visually compare all privacy-sensitive derivatives. Do not regenerate from HEIC originals or touch redactions. This trades additional static storage and a reproducible generation step for reduced transfer. Verify before/after bytes and lab metrics using the same version and settings.

### A11Y-01: insufficient gallery text contrast — verified

Lighthouse axe-core 4.13.0 flags `.gallery-section .section-heading > p`: foreground `#66706d` on `#eae9e2`, ratio 4.2:1 versus required 4.5:1 for this 16px normal text. Darken this foreground or shared muted color and rerun the audit.

### A11Y-02: accessible name excludes brand label — verified

`.wordmark` shows `L200 / HPE-S` but aria-label is `Voltar ao início`. Include visible text in accessible name, e.g. `L200 / HPE-S — voltar ao início`, and rerun the audit.

### UX-01: longer SEO H1 can displace CTA — inferred from verified layout

Browser via CUA checked 320x720, 390x844, and 1440x1000 viewports. Document scrollWidth equals viewport width in all three, with no horizontal overflow. At 320px CTA top is 704px and bottom 757px; at 390px CTA top 668px and bottom 721px. Baseline H1 is 166px high at 390px. Desktop 1440px H1 is 190px high, CTA top 580px. A longer H1 using the existing giant font will likely lengthen the hero. Preserve semantic title while using a smaller location/year span or carefully tuned typography; verify resulting narrow-screen layout and CTA access.

### HOST-01: cache and compression findings are local-server artifacts — verified limitation

Python preview sends no cache lifetime/compression; Lighthouse reports these. Hosted HEAD requests verified HTML gzip encoding and `Cache-Control: max-age=600` on HTML and the hero JPEG. Compression warnings are preview artifacts; the 10-minute hosted cache lifetime is controlled by GitHub Pages. Hosted Last-Modified changed during the audit (2026-10-03 03:16:38 UTC), so refetch production in final acceptance rather than relying on the initial drift snapshot. CSS is 10KB and measured render-blocking saving was about 110ms in mobile simulation; prioritize images over fragile critical-CSS extraction.

### DEPLOY-01: local and live drift — verified, external acceptance required

Production still serves the earlier layout. Final local evidence must remain labeled local until deployment and live URL re-audit. Search Console access, actual indexing, field metrics, query impressions/clicks/rankings remain unverified.

## Re-audit acceptance

- Both accessibility findings resolved in fresh Lighthouse results.
- Responsive candidates transfer fewer bytes while all 17 full-photo links and privacy edits remain intact.
- No horizontal overflow at 320, 390, 700, 1440 pixels; hero and CTA remain legible.
- Compare same Lighthouse version/settings; state simulator versus observed measurements.
- Treat SEO 100 as a narrow automated technical score, never as ranking or indexing proof.
- Stop the specialist-owned localhost server after final checks.

## Superseding baseline: externally updated dark design

The checkout fast-forwarded externally during the task to `7a07e4d78205a0a1012998005ab94baf43a9bac6`. Team writes were paused while this second baseline was measured. No team correction is credited for external changes.

HTML SHA-256: `21d16a0b6e87a30cb2cba2402267afb7357da0d5afce238a752d17ee6c98d7e9`. CSS SHA-256: `39d7ff5980bc1ac8966b944d3ee1df438a1c95b4a591ebb344208617d3ac7840`. This matches the initial live HTML snapshot.

Same Lighthouse 13.5.0 commands/settings, output paths `/tmp/l200-seo-dark-baseline-mobile.json` and `/tmp/l200-seo-dark-baseline-desktop.json`. Those runs are the authoritative before-comparison for SEO implementation.

```json
[
  {
    "device": "mobile",
    "scores": {
      "performance": 70.0,
      "accessibility": 100,
      "best-practices": 100,
      "seo": 100
    },
    "metrics": {
      "first-contentful-paint": 2788.588,
      "largest-contentful-paint": 10877.534,
      "total-blocking-time": 0,
      "cumulative-layout-shift": 0.038,
      "total-byte-weight": 5474811
    },
    "observedLCP": 344,
    "imageSavings": 4787563
  },
  {
    "device": "desktop",
    "scores": {
      "performance": 91.0,
      "accessibility": 100,
      "best-practices": 100,
      "seo": 100
    },
    "metrics": {
      "first-contentful-paint": 776.704,
      "largest-contentful-paint": 1922.478,
      "total-blocking-time": 0,
      "cumulative-layout-shift": 0.006,
      "total-byte-weight": 5739891
    },
    "observedLCP": 200,
    "imageSavings": 4956252
  }
]
```

Disposition: `A11Y-01` and `A11Y-02` are **superseded-by-external-design**, not resolved by this task; fresh dark baseline scores accessibility 100. `PERF-01` remains verified and more pronounced: nearly all full JPEGs are transferred in the lab navigation. Google Fonts now introduce external requests. `UX-01` must be rechecked against the new dark hero and intended longer H1; previous light-layout coordinates are not candidate acceptance thresholds. `HOST-01` hosted compression/cache observations remain applicable snapshots; `DEPLOY-01` will require final local/public hash comparison.
