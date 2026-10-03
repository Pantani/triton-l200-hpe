# SEO harness inventory and design

- Producer: orchestrator
- Consumer: SEO specialists and final reviewer
- Completion: audit-complete
- Baseline: `5df6296`, inspected 2026-10-03; clean checkout before this run.

## Inventory

```yaml
existing_skills: []
existing_roles: []
existing_repo_agents_file: false
existing_harness_docs: []
existing_runtime_profiles: []
detected_runtimes: [shared-workspace-workers, shell, web, browser]
stale_artifacts: []
compatibility_risks:
  - Shared filesystem ownership is advisory, not mechanically enforced.
  - Public HTML can differ from the local checkout.
  - Search Console access and search-index coverage are unverified.
  - Host-root robots and sitemap belong to another repository.
recommended_action: new minimal portable SEO harness
```

## Domain and reuse

Improve discovery of one private-sale Mitsubishi L200 Triton Sport HPE-S listing
for buyers in São Paulo state. The vehicle location is Zona Sul, São Paulo city.
Reuse the static HTML/CSS, existing privacy tests, photo assets, README, and the
`site/`-only Pages deployment boundary. Do not infer delivery, financing,
transmission, drivetrain, ratings, or stock history from the model name.

## Architecture decision

Fan-out/Fan-in for independent technical, regional-content, and performance
audits; Producer-Reviewer for implementation and re-audit. A single orchestrator
owns synthesis. This gives independent coverage without parallel edits to HTML.
No additional application framework, backend, agent runtime, or recursive team.
One shared checkout is sufficient with declared non-overlapping ownership and
serialized product writes. Existing user changes must remain intact.

## Task inventory and acceptance

1. Capture technical, content, and performance baseline reports.
2. Define reusable skills and explicit role/handoff contracts.
3. Correct metadata, truthful regional copy, structured offer, and discovery files.
4. Measure performance before changing image quality; preserve privacy edits.
5. Run existing tests plus meaningful structured-data/discovery consistency checks.
6. Independently re-audit, resolve local findings, and account for external gaps.
7. Exercise normal, missing-access, conflicting-writer, and near-miss harness cases.

## Initial environment issue

System Python could not import Pillow. A temporary virtual environment outside
the repository is used with the existing pinned requirements; this is not a
product defect. No baseline test success is claimed until that environment runs.

## Authorization

The user explicitly requested the specialist harness, implementation of the
previous audit recommendations, re-audit, and coverage of all findings. This
authorizes repository work and read-only external checks. Publishing, Search
Console changes, paid services, and messages to third parties are separate
external actions, not implied by a local verification result.

## Drift amendment

During the baseline audit an external `git pull --ff-only` advanced HEAD to
`7a07e4d`, including the `ce8f316` dark redesign. The team paused HTML/CSS writes,
preserved that design and repeated the performance baseline. Earlier light-theme
contrast/accessible-name findings are superseded by the external change, not
credited as this team's fixes. The current design is the comparison baseline.

Search Console access was subsequently discovered through the existing host-root
property. Following the user's request to execute the preceding audit actions,
the coordinator tested the public URL and requested indexing. Google accepted
the request. This resolves access uncertainty and request submission, not actual
index inclusion; see `02_search_console.md`. Site publication remains separate.
