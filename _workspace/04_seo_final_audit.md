# SEO remediation and final finding ledger

> Historical first-round snapshot. The user subsequently authorized publication
> and follow-up remediation. Current status and superseding dispositions are in
> [06_publication_followup.md](06_publication_followup.md). The former DNS blocker
> below no longer applies; keep it as evidence of the earlier observation only.

- Producer: SEO orchestrator
- Consumer: site owner and future SEO operators
- Date: 2026-10-03, America/Sao_Paulo
- Completion: local corrections and independent re-audit complete; external domain migration blocks final canonical/publication acceptance
- Current base: `c32b22d`; external redesign and source-photo cleanup preserved.
- Scope: the static listing, reusable SEO team, independent re-audit and the
  authorized index-request action. No commit, push or deployment by this team.

## Result and evidence

Three specialists audited technical SEO, regional content and performance. The
technical worker implemented the candidate; content and performance workers
independently reviewed it. Two repair rounds addressed image sharpness/mobile
contact layout and external font blocking. The coordinator retained synthesis
and publication boundaries throughout. Shared-path ownership was advisory,
explicit and non-overlapping, not a mechanical file lock.

The reusable entry point is `.agents/skills/seo-orchestrator/SKILL.md`, backed by
three specialist skills and `docs/harness/seo/team-spec.md`. Four skills passed
frontmatter/reference checks; five routing/failure/near-miss scenarios passed
contract simulations. Runtime crashes and permission failures were not injected.

Evidence:

- Baselines: `01_technical_audit.md`, `01_content_audit.md`, `01_performance_audit.md`.
- Implementation: `02_technical_implementation.md`.
- Live Google actions and validation: `02_search_console.md`.
- Independent reviews: `03_content_review.md`, `03_seo_review.md`.
- Harness validation: `03_harness_validation.md`.

## Complete finding ledger

| Finding | Final local disposition | Evidence and external acceptance |
| --- | --- | --- |
| T01 / C01 / C02 / C04 — regional title, H1 and description | resolved-local | Model, true HPE-S variant, year, sale intent and São Paulo are visible and consistent. Content review passed; live parity waits for publication. |
| C03 — useful regional content | resolved-local | One true capital location and visit information for buyers elsewhere in SP. No fictional local offices, delivery or city-page duplication. |
| T02 — discovery sitemap | resolved-local; external-pending | One exact canonical URL in valid sitemap XML. Serve it publicly and submit it using existing root Search Console property after deployment. Root robots already allows crawl; project-subpath robots is unnecessary. |
| T03 — vehicle/offer markup | resolved-local; officially code-validated | Product+Car/Offer matches price, location, images and qualified facts. Google Rich Results Test returned one valid Product snippet. Three optional warnings are explained below. |
| T04 / C05 / DEPLOY-01 — publication parity | external-pending | Local implementation is not public deployment. Owner/release operator must publish the approved candidate, then re-fetch HTML, CSS, fonts, images and sitemap. |
| T05 — actual index status | verified-live; inclusion pending | Existing root-property URL Inspection confirmed URL unknown/not indexed. Live test approved access; Request indexing was accepted into a priority crawl queue. Actual inclusion, canonical choice and search performance require later observation. |
| T06 — regression coverage | resolved-local | SEO tests cover canonical/sitemap, JSON-LD/visible price, correct place nesting, forbidden claims, asset existence, crawl directives, responsive pixel widths, local fonts and licenses. |
| PERF-01 — excessive image transfer | optimized-local; mobile LCP residual | Transfer reduced 68.5%; responsive WebPs retain original full-image links. Hero intentionally uses full resolution after R01 demonstrated visible blur. Simulated mobile LCP remains 7.35s; do not label mobile performance fully solved. |
| A11Y-01 / A11Y-02 — old theme contrast/name | superseded-by-external-design | External redesign removed these findings before this team's product edits. Dark baseline accessibility was already 100; no credit claimed for the team's fixes. |
| UX-01 / R02 — mobile heading and contact | resolved-local | Smaller narrow-screen title and spacing retain semantic title while bringing CTA forward. Independent 320/390/700/1440px review checks overflow and access. |
| HOST-01 — preview cache/compression warnings | not-needed-with-evidence | Public host was verified to gzip HTML and set a 10-minute cache; plain preview warnings do not prove production defects. Host-level policies are outside this site's source. |
| R01 — blurry mobile hero candidate | resolved-local | Full 1453px WebP preserves detail in tall cover crop; gallery stays responsive. Deliberate transfer-size trade-off. |
| R03 — gallery coverage lost during external cleanup | resolved-local | New public-only invariant compares gallery sources with every approved JPEG, independent of deleted private HEIC originals. |
| R04 — blocking Google Fonts dependency | resolved-local | Same typefaces served from 8 official WOFF2 files, OFL licenses/provenance retained; one small heading-font preload. Independent final network traces show zero external requests. |
| E01 — external host migration during final read-back | blocked-external, owner clarification pending | On final GET, the original canonical and sitemap returned HTTP301 to `http://pantani.xyz/triton-l200-hpe/` and its sitemap. Following the redirect failed DNS resolution. Confirm the intended HTTPS destination and repair DNS/TLS before changing canonical/schema/sitemap URLs or claiming publication readiness. |

## Newly observed domain change

The final public read-back on 2026-10-03 at 03:39 UTC observed GitHub-issued
HTTP301 responses to `http://pantani.xyz/triton-l200-hpe/` and its sitemap path.
The redirected host did not resolve through the test environment. This happened
after the successful Google live test and accepted indexing request; those
earlier results do not prove the new destination is accessible. The team did not
change the domain, DNS or hosting settings. The owner was asked to confirm the
definitive URL. Local URLs deliberately remain unchanged until that answer.

## Google evidence and honest limits

The exact public URL was not indexed when inspected. Google accepted an index
request after a successful live test. This is **request acceptance**, not proof
of index inclusion or a ranking improvement. The request concerns the current
public URL; uncommitted corrections are not thereby published.

Official candidate-code result:
https://search.google.com/test/rich-results/result?id=qDj8ifmJRR_rUpgfCBAhiw

One valid Product snippet; optional warnings for `aggregateRating`, `review`,
and `availability`. Ratings/reviews were not invented. Current inventory status
was conservatively left unasserted. These warnings do not invalidate this
product-snippet code test. Production enhancement detection remains separate.
Account screenshots are outside the repository in the chat visualization folder.

## Verification and preservation

The coordinator ran the current suite successfully: **19 tests passed** using
`/tmp/l200-seo-venv/bin/python -m unittest discover -s tests -v`. The temporary
environment uses the existing pinned Pillow 12.3.0; no application framework or
runtime dependency was introduced. `git diff --check` passed at review.

All 17 approved JPEGs were byte-identical to the tracked originals. All 51 WebP
derivatives contain no EXIF/XMP/ICC payload. Tests exercise display orientation,
no upscaling, missing source failures, and full public-gallery coverage. Pixel
and browser review complement metadata checks. Generated files add about7.21MB
of static storage in exchange for less visitor transfer; original photo detail
remains available via JPEG links.

## Final laboratory comparison

Lighthouse 13.5.0 / Chrome 154, same settings before and after, single-run local
navigation with simulated throttling. These are not field Core Web Vitals.
The coordinator independently read the final JSON reports; full method and
intermediate repair results are in `03_seo_review.md`.

| Metric | Mobile before | Mobile final | Desktop before | Desktop final |
| --- | ---: | ---: | ---: | ---: |
| Performance score | 70 | 75 | 91 | 96 |
| FCP | 2.79s | 1.65s | 0.78s | 0.36s |
| Simulated LCP | 10.88s | 7.35s | 1.92s | 1.36s |
| Transfer | 5.47MB | 1.73MB | 5.74MB | 1.81MB |
| Accessibility / best practices / automated SEO | 100 / 100 / 100 | 100 / 100 / 100 | 100 / 100 / 100 | 100 / 100 / 100 |

Transfer decreased about 68.5% on both. No horizontal overflow at 320, 390, 700
or 1440px; all 19 rendered image instances loaded. Mobile hero sharpness and
font styling were visually checked. The final mobile LCP remains a measured
performance limitation. Further optimization should compare deployed conditions
and photo quality; the two repair rounds do not justify an all-green claim.
Temporary preview servers were stopped and viewport overrides reset.

External work advanced the checkout first to the dark redesign (`7a07e4d`) and
then source cleanup (`c32b22d`). The team preserved both, rebaselined the actual
design and replaced the removed HEIC-dependent gallery invariant without
restoring deleted originals. Those external commits are not SEO-team changes.

## Remaining external actions

1. Site owner/release operator: publish the reviewed `site/` artifact; verify the
   exact canonical page, sitemap, new font and WebP URLs return expected content.
2. SEO operator: submit `https://pantani.github.io/triton-l200-hpe/sitemap.xml`
   through the existing `https://pantani.github.io/` Search Console property once
   it returns200. A root-sitemap edit is an alternative, not an additional must.
3. SEO operator: check actual index inclusion and Google-selected canonical after
   processing. Do not repeatedly request indexing to seek higher queue priority.
4. Owner: keep visible/structured price, mileage and sale state synchronized.
   Once data exists, compare page-filtered impressions/clicks/CTR/position over
   equal periods. No query volume or organic uplift was established here.
