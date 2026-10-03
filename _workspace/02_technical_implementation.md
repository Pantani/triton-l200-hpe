# Technical and regional SEO implementation

- Producer: technical SEO specialist
- Consumer: SEO orchestrator, content reviewer and independent SEO reviewer
- State: implemented; local automated checks pass; independent review pending
- Snapshot: shared checkout HEAD `7a07e4d`, with assigned uncommitted SEO changes; 2026-10-03
- Skill: `.agents/skills/seo-technical/SKILL.md`
- Ownership: `site/index.html`, `site/styles.css`, `site/sitemap.xml`, `tests/test_seo.py`, this report. Image generation/assets belong to coordinator.

## Baseline drift resolved before edits

The shared checkout advanced externally from the earlier light layout to HEAD `7a07e4d`, which includes dark-layout commit `ce8f316`. Writes paused until coordinator confirmed preservation of the new layout and the performance specialist completed a new baseline. The old light-layout muted-text contrast and wordmark accessible-name findings are superseded; dark baseline accessibility scored 100 in the independent lab. No gratuitous color/aria changes were made.

The dark layout has 19 image instances (hero, highlight, 17 gallery photos), an existing location FAQ and externally hosted fonts. The implementation preserves that design and all JPEG links; the old report's statements about absent location FAQ and only 18 image instances are superseded by this inspected snapshot. Current publication acceptance still requires live verification after deployment.

## Changes and rationale

- Title/social title and description prioritize HPE-S, sale intent, year, São Paulo, mileage and public price. One H1 includes all identifying information, with year/location on a smaller block span to limit its impact on mobile contact visibility. Model identity was not shortened to HPE.
- Added truthful capital/statewide visit information without claiming delivery, remote transaction support, financing or presence in other cities. Restored FAQ precision about city/location and coordinating a visit before traveling. Existing attributed history/maintenance answers remain.
- Replaced the gallery heading `Sem filtro` with descriptive `Fotos da L200`; the existing privacy-edit notice remains, avoiding an implication that the approved photos were unedited.
- Added static Product+Car JSON-LD and one Offer with price 159900 BRL, used condition, canonical URL, approved JPEG images and city-level location through Place/PostalAddress. Year and approximate mileage stay textual qualified PropertyValue facts rather than an invented full date or exact current mileage. No ratings, VIN, street address, policies, inventory duration or business identity were invented.
- Added a one-URL sitemap; no speculative lastmod or ineffective project robots file. Root robots/sitemap remain outside this repository's publication boundary.
- Added WebP source candidates for all 19 image instances with original JPEG fallbacks and original full-image links. Width/height match EXIF-oriented display dimensions. Gallery and split-picture CSS retains the existing fixed-height crops. Mobile/desktop sizes were calculated from the new 1280px outer container, 48px horizontal padding, 8px gallery gaps and 56px split gap. Hero is full viewport width. The coordinator generated all derivatives from approved JPEGs.

## Verification evidence

Before implementation, the six new invariant tests produced four failures and one missing-sitemap error (JSON-LD absent; responsive sources absent; sitemap absent); the non-blocking index-directive check already passed. These failures were expected missing features, not a clean baseline.

After implementation and coordinator image generation:

```text
rtk proxy /tmp/l200-seo-venv/bin/python -m unittest discover -s tests -v
Ran 17 tests in 0.074s
OK
```

The six new checks verify canonical/sitemap agreement, structured/visible price agreement, correct Place nesting and excluded unsupported/private fields, resolvable schema images, absence of index blocking, and the actual pixel width of every responsive candidate. Existing checks still cover owner facts, direct contact, public-file boundary, JPEG metadata and 17-photo gallery completeness. Coordinator tests cover generated-image orientation, metadata, non-upscaling and missing-input failures. New persistent test functions are small and unnested except bounded asset loops; no suppression added.

These tests establish source/artifact consistency, not Google index inclusion or rich-result validation. Rendered mobile/desktop acceptance belongs to the independent reviewer, who should check hero wrapping/contact position, picture cropping and source selection.

## Finding disposition

| ID | State | Evidence / next acceptance |
| --- | --- | --- |
| T01 / C01 / C02 / C04 | resolved-local, review pending | Metadata/H1 now identify truthful regional purchase intent; content review and rendered wrapping pending. |
| T02 | resolved-local + external-pending | Sitemap exists and XML/canonical test passes; host-root reference or Search Console submission remains external. |
| T03 | resolved-local, review pending | Parsed Product+Car/Offer with price, location and assets verified; no Google rich-result test result claimed. |
| T04 / C05 | external-pending | Live postdeployment parity is not established by this implementation. |
| T05 | verified-live, follow-up pending | Coordinator accessed the existing host-root Search Console property and inspected the exact listing: “URL is not on Google”, “URL unknown to Google”, no referring sitemap/page, no last crawl. Index request subsequently succeeded according to coordinator evidence; actual inclusion and search-performance history remain unverified. |
| T06 | resolved-local | Six new invariant checks pass with the existing suite. |
| C03 | resolved-local, review pending | New baseline already had basic location FAQ; enhanced location/statewide visit text now implemented. |

No commit, push, deployment, Search Console submission, root-host edit or external message was performed by this specialist. Ownership is now frozen for independent review; send requested repairs through the coordinator.

## Review repair round 1 — R01

Independent mobile review observed that `sizes="100vw"` selected the 480px hero at a 390px viewport with DPR 1, while the portrait cover crop scaled the landscape image much larger. This reduced visible vehicle sharpness. The hero now offers only its full 1453px WebP; the gallery/highlight keep responsive choices and every original JPEG fallback/link remains intact. This deliberately trades some mobile hero transfer size for reliable detail in the existing cover composition. The candidate-width test now permits any nonempty candidate set while still validating every declared width against actual pixels. Hero alternative text also identifies the genuine HPE-S trim and view. Postrepair measurements belong to the independent reviewer.

The coordinator's successful Search Console access supersedes the baseline assumption that the account was unavailable. The report retains the original baseline evidence but now records verified non-indexing rather than guessing index state from public search. The indexing request is an action, not proof that Google indexed the listing.

### R02 — narrow mobile heading and contact visibility

The same reviewer found that the 320px layout's four large heading lines plus location pushed the main contact action to y840, below the 720px viewport. In the same bounded repair round, a max-width 390px rule sets the title to 48px, location line to 18px, hero top padding to 112px, bottom padding to 48px and grid gap to 18px. This reduces vertical consumption while retaining every factual title term and keeping the desktop design unchanged. The persistent header contact remains available, but it was not used as a reason to dismiss the main-action finding. Independent browser inspection must confirm final positions and readability at 320px and 390px.

Postrepair verification: `rtk proxy /tmp/l200-seo-venv/bin/python -m unittest discover -s tests -v` passed all 16 currently present tests (0.075s). The current suite has three image-generation tests, six SEO tests and seven public-site tests; the previously observed source-photo-count test is no longer in the concurrently maintained public-site suite. No source consistency failure remains; visual/measurement re-audit is pending.

## Review repair round 2 — R04 local font delivery

The independent reviewer measured the external Google Fonts stylesheet as render-blocking (FCP 2.949s, estimated 2.15s opportunity). To address that measured dependency while preserving the redesigned typography, the coordinator assigned local font delivery as the final bounded repair round.

Fetched the exact existing Google Fonts family/weight request with a modern Chrome user agent. The observed official stylesheet returned WOFF2 URLs on `fonts.gstatic.com`; only latin and latin-ext faces were retained. Eight distinct original binaries now live in `site/assets/fonts/`, totaling 133,312 bytes on disk. Each HTTP response had `Content-Type: font/woff2` and each file has the `wOF2` signature. IBM Plex Sans 400/500/600 used identical per-subset URLs in the observed response, so three explicit weight mappings reference the same two files without binary duplication. Barlow Condensed 600/700 and IBM Plex Mono 500 retain their exact original mappings. Unicode ranges and `font-display: swap` are preserved.

`site/fonts.css` replaces the remote stylesheet; the two external preconnects were removed. The only font preload is the above-the-fold Barlow Condensed 700 latin face (14,888 bytes), which matches the display heading. The page does not preload all subsets or body weights. This adds repository-managed font assets and license maintenance in exchange for eliminating remote font stylesheet/connection dependency; the independent final run determines the observed rendering benefit.

Three unmodified SIL Open Font License files were fetched from the official `google/fonts` repository and ship beside the fonts. `site/assets/fonts/SOURCES.md` records original stylesheet URL, request user agent, exact asset URLs, sizes, hashes, content types and license sources. No font binary conversion or renaming of family metadata was performed.

Meaningful regression coverage was added first: the remote-font dependency test failed on the original external links. It now confirms no Google font links remain and all CSS font URLs resolve to local WOFF2 binaries. A second test verifies every CSS font family has its shipped OFL. Final `rtk proxy /tmp/l200-seo-venv/bin/python -m unittest discover -s tests -v` passed all 19 tests in 0.074s (the coordinator also added public-gallery derivative coverage during this round).

Files are frozen for the final independent mobile/desktop measurements. Two repair rounds are now exhausted; any remaining findings must be reported with evidence and disposition rather than hidden behind a perfect-score claim.
