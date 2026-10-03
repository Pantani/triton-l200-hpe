---
name: seo-review
description: Use when independently re-auditing SEO changes, measuring listing performance, or reconciling all findings before completion.
---

# SEO review and performance

## When to use

Use after changes or to establish a performance baseline before optimization.
The reviewer must remain independent of the candidate's implementation.

## Required inputs

Original request, frozen candidate, all baseline reports, measured baseline
environment and `docs/harness/seo/team-spec.md` acceptance contract.

## Workflow

1. Establish the audited snapshot and whether it is local or published.
2. Recheck every baseline ID, metadata, content truth, structured data, sitemap,
   public asset references and privacy/publication boundaries.
3. Measure mobile and desktop with tool version, viewport and throttling method.
   Inspect heading wrapping, contact visibility, focus, contrast and image load.
4. Compare the same measurement conditions after any optimization. Do not reduce
   image quality without evidence or overwrite privacy-edited source images.
5. Record new issues with R-prefixed IDs; never silently fix your own review
   target. Return pass/fix/partial, evidence and explicit remaining actions.
6. Test the harness's normal, missing-access, conflict and near-miss scenarios.

## Expected outputs

`_workspace/01_performance_audit.md` and `_workspace/03_seo_review.md`. Temporary
browser artifacts are owned by the reviewer and kept outside `site/`.

## Validation notes

Run relevant tests yourself; do not treat another worker's claim as evidence.
Lab metrics are not field Core Web Vitals, and a Lighthouse SEO score does not
prove indexing, local relevance or rankings. When a browser/tool/access is
unavailable, retain static checks and name the missing coverage.

## Primary references

- https://developers.google.com/search/docs/appearance/page-experience
- https://web.dev/articles/vitals
