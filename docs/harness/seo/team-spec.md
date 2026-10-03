# SEO specialist team

## Purpose and topology

Improve this static private-sale listing for relevant São Paulo searches using
verified facts and primary sources. Pattern: **Fan-out/Fan-in**, followed by
**Producer-Reviewer**. Maximum topology: coordinator → three workers. No nested
spawning. Portable skills and this contract remain usable without native agent
profiles. Use a single specialist for a narrow request; a spelling correction
does not require the team.

## Roles and ownership

| Role | Responsibility / required inputs | Skill | Allowed writes | Completion output |
| --- | --- | --- | --- | --- |
| Orchestrator | User scope, inventory, assignments, synthesis and acceptance | `seo-orchestrator` | Harness docs/skills, AGENTS.md, README, final ledger; product edits only after explicit ownership transfer | `_workspace/04_seo_final_audit.md` |
| Technical | HTML, deployment boundary, primary search/schema docs; crawlability and offer consistency | `seo-technical` | Assigned HTML, sitemap, SEO tests; own audit/implementation reports | `_workspace/02_technical_implementation.md` |
| Content | Visible owner facts, audience, technical proposal; truthful regional relevance | `seo-content` | Own reports only; propose HTML changes through coordinator | `_workspace/03_content_review.md` |
| Performance/reviewer | Frozen candidate, original request, all findings, baseline measurements | `seo-review` | Own reports and temporary browser artifacts only | `_workspace/03_seo_review.md` |

All roles may read public repository source, their handoff files, and relevant
public primary documentation. Never expose private documents, plate identifiers,
EXIF location, personal addresses, or private negotiation prices. Owner claims
remain attributed claims; source-code consistency does not certify the vehicle.

Workspace preference: shared checkout with advisory non-overlapping ownership.
The coordinator announces assignment and transfer through the native channel.
If overlap occurs, stop those writes and serialize; do not claim mechanical
exclusivity. Reviewers never silently rewrite the candidate they are grading.
Temporary servers and reports have unique paths/ports and an explicit owner.

## Permissions and communication

Default deny. Assigned workers may read repository files, use shell and public
network for verification, and write only the paths above. No external mutations,
publish, purchases, credential inspection, new branches, or spawning. The
coordinator handles clarifications, escalation, and final synthesis. Model
policy: `inherit`, with evidence-based reasoning and tool capability required.
`runtime_overrides: {}`; concrete runtime/model pins are unnecessary.

Use native messages for short status. Preserve decisions, findings, evidence,
and acceptance in the named artifacts. Never count a missing worker as a pass.

## Phase outputs and handoffs

Every report starts with producer, consumer, completion state, and audited
snapshot/environment. Findings use `ID | severity | evidence | action |
acceptance | state`; retain IDs across repair rounds.

| Phase | Producer → consumer | Artifact | Required content |
| --- | --- | --- | --- |
| 0 inventory/design | Coordinator → specialists | `_workspace/00_contract_inventory.md` | Existing contracts, domain, scope, pattern, runtime limits |
| 1 baseline | Technical → coordinator | `_workspace/01_technical_audit.md` | Crawl/schema/discovery findings, primary sources |
| 1 baseline | Content → coordinator | `_workspace/01_content_audit.md` | Query intent, factual boundary, proposed text |
| 1 baseline | Performance → coordinator | `_workspace/01_performance_audit.md` | Lab method, measurements or explicit unavailable status |
| 2 implementation | Technical → reviewers | `_workspace/02_technical_implementation.md` | Files, tests, decisions, known gaps |
| 2 optional external check | Coordinator → reviewer | `_workspace/02_search_console.md` | Exact property/URL, index evidence, authorized action and outcome; no credentials |
| 3 review | Content → coordinator | `_workspace/03_content_review.md` | Original IDs, regressions, disposition |
| 3 review | Independent reviewer → coordinator | `_workspace/03_seo_review.md` | Re-audit and all local acceptance checks |
| 3 harness test | Coordinator → future operators | `_workspace/03_harness_validation.md` | Normal/failure/near-miss scenarios and results |
| 4 final synthesis | Coordinator → user | `_workspace/04_seo_final_audit.md` | Every finding, evidence, residual owners and next actions |

## Execution and acceptance

1. Inspect drift, clean/dirty state, facts, live URL and existing contracts.
2. Assign independent audit branches against the same snapshot before edits.
3. Synthesize findings. Assign one HTML writer; content provides proposals.
4. Implement only justified changes. Retain existing photo privacy edits and
   public-gallery coverage. Use meaningful invariant tests, not copy snapshots.
5. Run `python3 -m unittest discover -s tests -v` with requirements installed;
   review HTML/mobile rendering, schema, canonical and sitemap consistency.
6. Freeze writes for independent review. Allow at most two repair/review rounds;
   any remaining material issue leaves the result `partial`, with next action.
7. Report `resolved-local`, `verified-live`, `external-pending`, or
   `not-needed-with-evidence` per finding. Local tests never prove indexing,
   ranking, rich-result eligibility, field performance, or production deployment.

## Failure and safe degradation

| Failure | Required behavior |
| --- | --- |
| Worker spawn/model/tool unavailable | Coordinator runs the slice sequentially; disclose reduced independence or missing measurements. |
| Resource conflict/workspace setup failure | Pause conflicting writes; serialize in the current safe checkout or isolate deliberately. |
| Worker partial failure/missing branch at synthesis | Preserve report, reassign missing work once, leave uncovered acceptance explicit. |
| Communication failure | Use the deterministic report as fallback; reconcile its snapshot before synthesis. |
| Permission denial/Search Console unavailable | Do not bypass access; provide exact external next action and mark external-pending. |
| Unsupported runtime capability | State the lost guarantee; manual review is not an automated test result. |
| Conflicting facts/reviewer disagreement | Prefer source evidence, omit unverified claims, retain disagreement until resolved. |
| Repair limit exceeded | Preserve candidate and evidence; finish partial, never manufacture a clean report. |

## Sources and scope boundaries

Use Google Search Central for search behavior and Schema.org for vocabulary.
Check live references before relying on eligibility or feature support. Schema
validation, rich-result validation, index inclusion, and ranking are separate
checks. Host-root robots rules belong to the root `pantani.xyz` hosting repository, not this project's
subdirectory. A one-page sitemap is a discovery aid, not a ranking promise.
