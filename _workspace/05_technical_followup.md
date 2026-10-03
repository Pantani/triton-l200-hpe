# Technical follow-up: canonical domain and publication candidate

- Producer: technical SEO specialist
- Consumer: coordinator / publication owner
- State: read-only review complete; local candidate accepted, live parity pending
- Snapshot: HEAD `e1a4465` plus uncommitted authorized SEO files, 2026-10-03
- Ownership: this report only. No browser actions, external mutations, product edits or commits.

## Acceptance evidence

| ID | Severity | Evidence | Acceptance / disposition |
| --- | --- | --- | --- |
| F01 | High | Verified local: canonical, og:url, og:image, Product @id/url/images, Offer URL and sitemap all use `https://pantani.xyz/triton-l200-hpe/`. No old host occurs in public HTML/CSS/XML/JSON. Updated invariant test also rejects old host and checks social/canonical parity. | Accepted locally. Historical audit reports legitimately retain the former observed host; those are not serving metadata. |
| F02 | High | Verified local: static page remains crawlable, single canonical; sitemap contains the exact new HTTPS trailing-slash URL. `rtk proxy /tmp/l200-seo-venv/bin/python -m unittest discover -s tests -v`: 19 tests pass, 0.074s. | Accepted locally; deployment owner must re-fetch the actual public page and sitemap after successful Pages run. |
| F03 | High | Verified HTTP at this review: new listing URL returns 200 but still old canonical; new project sitemap returns 404. Old github.io listing request ends at the new domain with 200. New host robots and root sitemap still returned old github.io references despite coordinator's reported root-repo commit. | Pending live publication/CDN parity. A root commit/push is not yet proof of observed deployment. Recheck root robots, root sitemap and listing sitemap after both workflows complete; do not duplicate the root file under the project path. |
| F04 | High | Verified local: no PDF/HEIC/env/key/PEM in public artifact, no private-identifier fields in public HTML/CSS/XML/JSON scan, no schema street address or VIN. Existing identifier/privacy tests pass. Pages workflow still uploads only `site/`. | Accepted source/publication boundary. This is source/metadata review, not renewed pixel inspection or proof all historical repository disclosures were erased. |
| F05 | Medium | Verified diff: intended changes are SEO metadata/copy/schema, responsive assets/generator, local fonts/licenses, invariant tests and requested harness/docs. `.gitignore` adds `.venv/`. Existing private original-photo deletion is already HEAD `e1a4465`, outside this task's changes. `git diff --check` passes. | Preserve current history; include required untracked public assets/fonts/CSS/sitemap/tests/tools in the publication commit. Committing only tracked HTML/CSS would create broken asset references. |

## Publication risks and required read-back

1. The Pages workflow triggers on main and installs the pinned Pillow dependency before running all tests. It publishes only `site/`; harness, reports and generators do not become website content. They remain repository content if committed.
2. Domain migration is internally consistent in the candidate, but the live response still showed the old canonical during this review. After the successful workflow, verify canonical/OG/schema/sitemap on the new domain and the old-domain redirect target. Verify no X-Robots-Tag or meta noindex appeared.
3. The root hosting change was reported by the coordinator as committed/pushed `1231f02`; this reviewer did not mutate or audit that other repository. HTTP responses at review time still showed old root content, so root-discovery correction remains awaiting public read-back.
4. The new project sitemap must return 200 before it is treated as successfully available to Search Console. A sitemap entry alone does not prove indexing. Inspect the new canonical URL in the applicable verified property; retain exact index-request and URL Inspection outcomes separately from later index inclusion or performance.
5. The performance specialist owns the additional image optimization and final rendered measurements. This review accepts technical metadata and publication boundaries only; it does not supersede that independent browser evidence.

No actionable local technical defect was found in the inspected migration candidate. Live deployment parity remains an explicit acceptance condition, not a speculative defect or an indexing guarantee.
