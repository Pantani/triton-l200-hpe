# Regional SEO and content baseline

- Producer: regional-content-specialist
- Consumer: SEO orchestrator and independent QA
- Date: 2026-10-03 (America/Sao_Paulo)
- Scope: `site/index.html` and public HTML at `https://pantani.github.io/triton-l200-hpe/`
- State: audit-complete; recommendations await implementation and re-audit
- Ownership: this report only; no product-file changes
- Method: direct source inspection and live HTML fetched using `rtk proxy curl -fsSL`; web fetch failed for the listing, so the successful curl response is the public-page evidence.

## Evidence boundaries

Snapshot drift update: the coordinator reported an external fast-forward during the task. A fresh source read at HEAD `7a07e4d78205a0a1012998005ab94baf43a9bac6` confirms that local HTML now uses the dark layout, its H1 is `Triton Sport HPE-S 2019/2020`, and the location FAQ is present. Preserve this newer source. The historical findings below remain a record of the first snapshot; C02 now includes restoring L200 to the local H1, C03 now means preserving and expanding the existing location answer rather than restoring a missing one, and C05 needs a new deployment comparison against the final candidate. Title and description recommendations remain applicable.

Verified here means verified as text present in the repository or fetched public page, not independently authenticated vehicle condition, ownership, maintenance history, availability, or specifications. The page identifies HPE-S, model year 2019/2020, black, diesel, approximately 53,500 km, advertised price R$ 159,900, private sale without trade-in, and location in Zona Sul of São Paulo. Maintenance, no auction history, and no accident history remain owner assertions. Preserve their attribution. Do not infer transmission, drivetrain, warranty, delivery, financing, exact address, or current odometer from trim names.

## Findings and acceptance

| ID | Severity | Evidence and interpretation | Acceptance |
| --- | --- | --- | --- |
| C01 | Medium | Verified: local and public `<title>` identify model/year and private sale, but omit São Paulo and explicit purchase wording. Inferred: adding the actual location and sale intent improves the relevance communicated to a prospective buyer; ranking uplift is unmeasured. | One descriptive title contains L200 Triton, HPE-S, year, sale intent, and São Paulo. Social title remains factually consistent. No repeated keyword variants. |
| C02 | Medium | Verified: local H1 is `L200 Triton Sport HPE-S 2019/2020.` without location; public H1 is `Triton Sport HPE-S 2019/2020`, omitting L200 too. | One visible H1 identifies L200 Triton Sport HPE-S, 2019/2020, sale intent, and São Paulo; check mobile wrapping after longer wording. |
| C03 | Medium | Verified: local page has location in eyebrow/contact but no substantive regional section or location FAQ; public page already answers `Onde posso ver o carro?` with Zona Sul and WhatsApp. | Preserve/restore truthful visit information, visibly explain capital location, and address buyers elsewhere in the state without claiming delivery or a presence in other cities. |
| C04 | Low | Verified: existing description puts location and price after maintenance/tires/audio. Inferred: prioritizing model, location, price and mileage better summarizes a purchase result. Its current length is not a technical failure; Google does not prescribe a fixed character limit. | One coherent description prioritizes model, actual location, mileage and advertised price; no fabricated urgency or rigid SEO length rule. |
| C05 | High operational | Verified: fetched public HTML is an older layout and differs from local source. Local content changes cannot prove public acceptance. | Re-fetch the published canonical URL after deployment and verify implemented title/H1/description/location facts; otherwise explicitly mark publication pending. |

## Recommended implementation copy

The following is proposed copy, not a claim of ranking impact. Product copy remains Portuguese; report prose is English.

- Title and social title: `L200 Triton Sport HPE-S 2020 à venda em São Paulo`
- H1: `L200 Triton Sport HPE-S 2019/2020 à venda em São Paulo`
- Description: `L200 Triton Sport HPE-S 2019/2020 diesel, cerca de 53.500 km, por R$ 159.900. Venda particular na Zona Sul de São Paulo. Veja fotos e combine uma visita.`
- Location heading: `Venda particular na Zona Sul de São Paulo`
- Location paragraph: `Esta Mitsubishi L200 Triton Sport HPE-S 2019/2020 está na Zona Sul da cidade de São Paulo. Veja as fotos, confira a ficha do veículo e fale diretamente com o proprietário pelo WhatsApp para combinar uma visita.`
- Statewide buyer paragraph: `Está em outra cidade do estado de São Paulo? Entre em contato para tirar dúvidas e combinar os detalhes de uma visita à capital.`
- Location FAQ: `Onde posso ver a L200 Triton?` / `Na Zona Sul da cidade de São Paulo, capital. Combine o local e o horário da visita diretamente com o proprietário pelo WhatsApp.`
- Statewide FAQ: `Moro em outra cidade de São Paulo. Como combinar uma visita?` / `Fale com o proprietário pelo WhatsApp antes de se deslocar à capital para combinar os detalhes da visita.`

The statewide wording is an invitation to ask, not a claim of delivery, logistics, or remote transaction support. Existing FAQ about trade-in, mileage, and owner-attributed history should stay. Do not add a keyword-driven HPE/HPE-S comparison without a genuine factual buyer need and verified differences.

## Baseline pressure scenarios

### Normal flow: accurate regional listing

Input: one privately advertised vehicle located in Zona Sul of São Paulo. Decision: one canonical page, accurate title/H1, concise description, location/visit text, truthful visible facts. Expected outcome: buyers can identify model, version, year, price and visit location without contacting the owner just to establish the city. Status: baseline audit passed; implementation pending.

### Failure flow: target every city and relabel HPE-S as HPE

Input: pressure to generate near-duplicate pages for all São Paulo cities and replace HPE-S with the shorter HPE query. Decision: reject both changes. The available listing identifies HPE-S; shortening the trim would contradict the source. City pages would add unsupported location impressions without distinct buyer value. Use natural statewide context on the same truthful listing. Ask for facts only if later work requires delivery, exact address or other unverified commercial terms; these unknowns do not block the safe copy above. Status: passed; no fabrication recommended.

## Primary sources checked

- [Google title links](https://developers.google.com/search/docs/appearance/title-link): descriptive concise title and clear main heading; Google may select other title sources. No ranking guarantee.
- [Google snippets](https://developers.google.com/search/docs/appearance/snippet): page content primarily supplies snippets; meta description may be used; truncation depends on presentation, not a universal character ceiling.
- [Google spam policies — doorway abuse](https://developers.google.com/search/docs/essentials/spam-policies#doorway-abuse): region/city pages that funnel users without distinct value are a documented abuse pattern.

## Unknowns and external dependencies

Search Console impressions, query demand, ranking, actual index inclusion, current listing availability, current odometer and owner records were not verified. Any outcome claim requires later Search Console measurements. Local content acceptance does not establish deployment or indexing.
