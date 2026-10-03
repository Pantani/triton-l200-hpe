---
name: seo-technical
description: Use when auditing or correcting crawlability, canonical URLs, sitemap discovery, or vehicle-offer structured data on a static listing.
---

# Technical SEO

## When to use

Use for search-engine access and machine-readable listing information. Regional
copy belongs to `seo-content`; performance measurements belong to `seo-review`.

## Required inputs

Canonical URL, deployment boundary, current HTML, owner-confirmed public facts,
public HTTP evidence, and assigned write paths from `docs/harness/seo/team-spec.md`.

## Workflow

1. Compare local and live snapshots. Inspect status, redirects, robots at the
   host root, indexing directives, canonical URL and discoverable sitemap.
2. Read current Google Search Central and Schema.org sources before selecting
   markup. Distinguish vocabulary validity from rich-result support.
3. For one used vehicle offered by contact, describe the actual `Product` and
   `Car` with `Offer`. Match visible price/currency/location and preserve owner
   attribution. Do not invent reviews, dates, identifiers, or checkout policies.
4. Keep absolute canonical/image URLs consistent. A project-subpath robots file
   does not replace the host-root file. Omit fake last-modified dates.
5. Add invariant checks for schema/visible-data agreement, canonical/sitemap
   agreement, resolvable public assets, and the site's publication boundary.
6. Report deployment drift and Search Console actions separately from local fixes.

## Expected outputs

`_workspace/01_technical_audit.md`, assigned changes, and
`_workspace/02_technical_implementation.md`, using stable T-prefixed finding IDs.

## Validation notes

Run repository tests, parse JSON/XML, inspect rendered HTML and relevant HTTP
responses. If indexing access is absent, mark it external-pending with a concrete
next action. Never claim rankings, indexing or rich-result display from tests.

## Primary references

- https://developers.google.com/search/docs/appearance/structured-data/product-snippet
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- https://developers.google.com/crawling/docs/robots-txt/create-robots-txt
- https://schema.org/Car
- https://schema.org/Offer
