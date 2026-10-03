# Independent regional-content re-review

- Producer: content specialist, independent of HTML/CSS implementation
- Consumer: coordinator and final independent reviewer
- Completion: pass for local content; deployment remains external-pending
- Snapshot: frozen `site/index.html`, SHA-256 `265f594e047ce9076028cb8713cdd1603d5dfe2b369a10bfb0ba669c2f5eabe4`, reviewed 2026-10-03
- Environment: shared checkout at base HEAD `7a07e4d78205a0a1012998005ab94baf43a9bac6` plus local SEO changes
- Ownership: review report only; no product edits
- Skill: `.agents/skills/seo-content/SKILL.md`

## Disposition of baseline findings

| ID | Severity | Evidence | Action | Acceptance | State |
| --- | --- | --- | --- | --- | --- |
| C01 | Medium | `site/index.html:20` title includes L200 Triton Sport, HPE-S, 2020, sale intent and São Paulo; `og:title` agrees. | No further local change. | Descriptive title with truthful actual city and preserved variant; no keyword list. | resolved-local |
| C02 | Medium | `site/index.html:96` contains the only H1, whose normalized text is `L200 Triton Sport HPE-S 2019/2020 à venda em São Paulo`. | Content accepted; visual wrapping remains part of independent browser review. | Complete identity/year, purchase intent and city in the main heading. | resolved-local |
| C03 | Medium | `site/index.html:178` retains the capital visit answer; lines 179 and 183–187 address other SP cities and the actual Zona Sul location. | No further local change. | Specific place and contact instructions without invented statewide delivery or branch locations. | resolved-local |
| C04 | Low | `site/index.html:7` description prioritizes model, approximate mileage, advertised price and Zona Sul. It equals the JSON-LD and social descriptions. | No further local change. | Useful concise summary and factual agreement; no rigid character-limit assertion. | resolved-local |
| C05 | High operational | Local candidate reviewed above has not been published, according to the coordinator's current status. Initial baseline drift was also amended after the external fast-forward. | Publish through the authorized workflow, then fetch the public canonical URL and compare final content. | Public title/H1/description/local content match the intended candidate. | external-pending |

## Truthfulness and consistency checks

Executed a separate Python standard-library extraction from the frozen HTML. JSON-LD parsed successfully; there is one H1; schema description equals the meta description. Manual comparison of visible copy and structured facts found consistent HPE-S, 2019/2020, black, diesel, approximate 53,500 km, R$ 159,900 and city/state. Approximate mileage is explicitly named rather than represented as an exact current odometer. The photo's 53,459 km is distinguished as the photographed reading.

The schema contains no invented transmission, drivetrain, VIN, ratings or review properties. It adds no precise street address or service-area/delivery claims. The visible FAQ continues to attribute auction/accident history and maintenance to the owner. Existing promotional maintenance/audio/tire statements are source-listed assertions, not independently authenticated facts; the implementation does not elevate them into new machine-readable certifications.

The exact statewide paragraph is `Está em outra cidade do estado de São Paulo? Entre em contato para tirar dúvidas e combinar os detalhes de uma visita à capital.` This is a contact/visit invitation, not a claim of transport, delivery, financing, remote sale, or service throughout the state. The corresponding FAQ tells buyers to contact the owner before traveling. No city-name list or duplicated regional page was introduced.

The gallery heading now says `Fotos da L200`, and the visible disclosure explicitly states that plates, property numbers and third-party data were hidden. This avoids the previous `Sem filtro` wording implying wholly unedited images. This review verified the disclosure and content, not every pixel or image metadata item; image privacy verification remains in technical/visual acceptance.

## New findings

No actionable new local content defect found in this frozen candidate. This is a scoped content acceptance, not a certification of vehicle history, rendered layout, live publication, indexing, or search ranking.

## Updated external evidence

The coordinator reported an actual read of the existing Search Console root property: the URL was not on Google/unknown, without a referring sitemap or page; the live test was still running at handoff. This worker did not independently operate Search Console. Do not carry the earlier hypothetical missing-access scenario forward as an actual blocker. The final ledger should cite the coordinator's direct observation and final live-test result, and distinguish a request for indexing from successful index inclusion.

## Remaining acceptance boundaries

- Independent browser review owns mobile/desktop heading wrapping and contact usability; source reading alone does not close that coverage.
- Public deployment and a read-back of the candidate are required to close C05.
- The owner's current commercial facts and mechanical condition were not independently authenticated in this audit.
- No ranking gain or query-volume claim is supported by these checks; later Search Console observation is a separate outcome measurement.
