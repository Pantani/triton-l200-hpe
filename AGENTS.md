# Repository guide

This is a static, single-page private-sale listing. `site/` is the complete
public artifact; GitHub Pages publishes only that directory. Keep public copy
in Brazilian Portuguese and code, tests, and documentation in English.

Preserve owner-provided facts and their attribution. Do not infer vehicle
features, delivery, financing, ratings, or an exact street address. Never copy
private documents, identifiers, or negotiation details into public assets.
Existing privacy-edited photographs must remain intact.

There is no application build step. Install `requirements-dev.txt` in a virtual
environment, then run `python3 -m unittest discover -s tests -v`. Preview with
`python3 -m http.server 8000 --directory site`. Follow any applicable shell
wrapper instructions from the user's environment.

For full SEO work, start with `.agents/skills/seo-orchestrator/SKILL.md` and
`docs/harness/seo/team-spec.md`. Assign one HTML writer at a time. Local tests
and browser measurements do not establish deployment, indexing, or ranking.
