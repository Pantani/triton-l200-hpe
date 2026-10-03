---
name: seo-content
description: Use when improving regional purchase intent, headings, snippets, or factual buyer information for this São Paulo vehicle listing.
---

# Regional listing content

## When to use

Use for title, H1, description, local context and buyer questions. Do not use to
invent SEO landing pages or certify mechanical condition from the listing text.

## Required inputs

Current visible copy, true variant/year/location, user target audience, price
and owner assertions. Read `docs/harness/seo/team-spec.md` for assigned outputs.

## Workflow

1. Inventory verified page statements and separate them from independently
   verified vehicle facts. Record unknown logistics and specification details.
2. Connect model, variant, sale intent and actual city in concise title/H1.
   Preserve HPE-S even if a query uses HPE. Avoid lists of keyword variants.
3. Put useful facts early in the description. Explain where visits occur and
   how to contact the owner; buyers elsewhere in SP do not imply delivery.
4. Use natural buyer questions and factual local context, without duplicated
   city pages, invented offices, fake ratings or unsupported superlatives.
5. Propose edits to the assigned HTML owner. Re-review visible and structured
   facts together, including mobile readability and owner attribution.

## Expected outputs

`_workspace/01_content_audit.md` with C-prefixed findings and proposed PT-BR copy;
`_workspace/03_content_review.md` with acceptance and unresolved factual gaps.
Reports are in English, while customer-facing copy remains PT-BR.

## Validation notes

Check the finished title, H1, description, local section and FAQ against source
facts. Distinguish recommendations from measured query volumes. A spelling-only
request needs a direct edit, not the full SEO team.

## Primary references

- https://developers.google.com/search/docs/appearance/title-link
- https://developers.google.com/search/docs/appearance/snippet
- https://developers.google.com/search/docs/essentials/spam-policies
