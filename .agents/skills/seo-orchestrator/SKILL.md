---
name: seo-orchestrator
description: Use when coordinating a full SEO audit, implementation, and independent re-audit of this private-sale listing, including external indexing gaps.
---

# SEO orchestration

## When to use

Use for an end-to-end SEO cycle spanning content, technical search signals and
performance. Keep a narrow copy correction direct; do not summon the full team.

## Required inputs

User scope, repository state, canonical public URL, confirmed listing facts,
available verification tools and access. Read `docs/harness/seo/team-spec.md`
from the repository root for role ownership and deterministic output contracts.

## Workflow

1. Inventory existing skills/contracts and drift; preserve user work.
2. Capture `_workspace/00_contract_inventory.md`. Assign independent technical,
   content and performance baselines using the team contract.
3. Synthesize IDs and priorities. Give one worker HTML ownership; serialize
   intersecting writes. Record whether ownership is advisory or enforced.
4. Implement verified corrections with relevant tests and preserve privacy.
5. Request independent re-audit against the original request and all baseline
   IDs. Resolve local findings within the bounded review loop.
6. Account for every finding in `_workspace/04_seo_final_audit.md`, distinguishing
   repository completion from live deployment and search-engine outcomes.

## Expected outputs

Named phase reports from the team spec, reusable specialist contracts, corrected
site, verification evidence and an explicit ledger of remaining external work.

## Validation notes

Exercise normal flow, missing Search Console access, writer conflict and a
near-miss spelling fix. On worker failure, retain partial evidence and use the
documented sequential fallback. A missing result is never an implicit pass.
No runtime-specific profile is needed to use this workflow.
