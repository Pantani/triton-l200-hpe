# SEO harness validation

- Producer: content specialist, explicitly delegated by coordinator for this artifact
- Consumer: coordinator and future operators
- Completion: structural-checks-passed; five simulated-routing-scenarios-passed
- Snapshot: four `.agents/skills/seo-*/SKILL.md` files and `docs/harness/seo/team-spec.md`, inspected 2026-10-03 before implementation completion
- Environment: shared checkout; report ownership is advisory and non-overlapping, not mechanically enforced
- Scope: contract structure and thought-exercise routing; this does not establish site acceptance, live deployment, tool recovery, or search performance

## Executed structural checks

A Python standard-library check read every SEO skill and confirmed the opening YAML-style frontmatter delimiters, nonempty `name` and `description`, directory/name agreement, and the five required sections: When to use, Required inputs, Workflow, Expected outputs, Validation notes. All four passed. This checks the actual simple frontmatter used here; it is not a general YAML parser validation.

Each skill's team-spec reference resolves to the existing file. Manual comparison confirmed agreement between expected-output paths and the phase table. `tests/` and `requirements-dev.txt` exist. The validation command in the team spec is therefore structurally grounded; this report did not execute site tests, which belong to the technical/reviewer stages.

Phase 0 and baseline artifacts already exist. Phase 2, review and final artifacts are future outputs at this snapshot, not broken source references. The team spec lists the coordinator as accountable producer for this harness validation; the coordinator explicitly delegated production to this content worker while retaining synthesis ownership. No native profile or concrete model identifier is required by the portable contracts.

## Simulated routing scenarios

These are thought exercises against the written contracts, not injected runtime failures or measured recovery tests.

| Scenario | Instructions exercised | Expected routing and result | Simulation outcome |
| --- | --- | --- | --- |
| Full SEO request | Orchestrator steps 1–6; team phase table and one-writer rule | Coordinator inventories current state; technical/content/performance workers independently baseline; technical owns HTML after assignment; content proposes; independent review follows a frozen candidate; coordinator reconciles every ID and distinguishes local/live/external states. | Pass: all phases have named outputs and ownership; no reviewer must edit its candidate. |
| Missing Search Console access | Technical validation notes; team permission-denial rule and acceptance states | Complete repo and public HTTP checks; mark index/performance verification `external-pending`; name owner action to inspect the canonical URL, submit sitemap and request indexing if appropriate. No credential bypass and no assertion that tests prove indexing. | Pass: loss of access does not silently become success or block independent local work. No actual Search Console failure was injected. |
| Competing HTML writers | Orchestrator step 3; team workspace and resource-conflict rules | Content worker stops before applying an HTML edit; coordinator gives one worker advisory ownership, or serializes explicit transfer after the current writer stops. Reviewers remain read-only. | Pass: contracts explicitly disclose advisory enforcement and forbid uncontrolled overlapping writes. No actual file race was created. |
| Spelling-only request | Orchestrator When to use; content Validation notes; team topology | Make the bounded copy correction directly using the relevant content guidance; do not start full fan-out or generate irrelevant SEO reports. | Pass: narrow request stays narrow. No product file was changed for this simulation. |
| Pressure to target every SP city and rename HPE-S to HPE | Content workflow 1–4; team privacy/factual boundaries; primary spam-policy reference | Preserve source-listed HPE-S; use one actual capital location and truthful statewide buyer invitation; reject duplicated city pages, invented offices and unsupported delivery. Record unknown logistics instead of inventing them. | Pass: guidance reaches the same factual boundaries as the baseline audit. No city pages or trim edits were created. |

## Actual snapshot drift event

Separate from the simulated writer-conflict test, the coordinator reported an external Git fast-forward and paused technical edits for rebaselining. A direct fresh read confirmed HEAD `7a07e4d78205a0a1012998005ab94baf43a9bac6` and a changed local HTML layout with the location FAQ present. The content baseline now includes an explicit amendment for C02/C03/C05, and the newer user layout must be preserved. This is observed snapshot drift plus coordinator-reported pause/rebaseline handling; it is not evidence of overlapping team writes or a mechanically enforced lock. Full resumed implementation acceptance remains with the later review.

## Honest baseline comparison

The manually produced `_workspace/01_content_audit.md` already recommended one factual regional listing, HPE-S preservation, owner attribution, and explicit publication uncertainty. The generated content skill reaches the same decisions in the pressure scenario. The observed benefit is making boundaries, handoff paths, assignment rules and incomplete states explicit for reuse. This exercise provides no evidence of better rankings, faster work, superior accuracy, or better recovery than a competent manual baseline.

## Coverage limits and handoff

- No runtime spawn failure, permission denial, worker crash, conflicting write or communication outage was induced. These remain simulated failure-policy coverage.
- Frontmatter and role-output consistency were checked; future acceptance still needs actual implementation/test/review reports.
- The baseline content report predates the formal six-column finding schema. Its rows already provide ID, severity, evidence, recommendation and acceptance, and the report declares implementation pending globally. The content re-review and final ledger should provide explicit per-ID state for deterministic closure.
- Do not treat future output paths as completed evidence until their producers have written them.
- Revalidate this report if role permissions, output names or ownership rules change.
