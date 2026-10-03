# Technical SEO baseline — 2026-10-03

- Producer: technical SEO specialist
- Consumer: SEO orchestrator / implementation owner
- State: audit-complete; implementation not started
- Scope: read-only local HTML, existing publication boundaries, public HTTP responses, primary documentation. No Search Console account evidence available.
- Ownership: this report only; no site or test writes.

## Verified baseline

`site/index.html` is static Portuguese HTML with one H1, absolute self-canonical, a public price and direct WhatsApp links. Owner fact authority is `docs/superpowers/specs/2026-10-02-l200-listing-site-design.md`, Public facts and copy. Current local HTML contains no JSON-LD. Public GET observations on 2026-10-03: listing 200, no X-Robots-Tag, host robots 200 with `User-agent: *`, `Allow: /`, host sitemap 200 containing only the portfolio root, project sitemap 404. Live HTML differs materially from local HTML (live loads Google fonts; local does not).

## Findings and acceptance

| ID | Priority | Finding / evidence | Acceptance / disposition |
| --- | --- | --- | --- |
| T01 | High | Verified: local and live title identify the car but omit São Paulo. Local H1 omits sale intent and location. Description already has those facts. | Title and primary visible heading combine genuine HPE-S identity, year, sale intent and São Paulo. Avoid relabeling the car HPE merely for a query. Content specialist owns copy. |
| T02 | High | Verified: project sitemap returns 404; host sitemap advertises only portfolio. This is a discovery gap, not evidence Google cannot crawl. | Add `site/sitemap.xml` with the exact HTTPS trailing-slash canonical. Parse XML in checks; validate live 200 after deployment. Omit speculative `lastmod`, priority and frequency. Root robots/sitemap edit belongs to another repo or Search Console submission and remains externally blocked until access is available. |
| T03 | Medium | Verified: no Product/Car JSON-LD despite one public vehicle offer. | Add a valid static Product+Car object and Offer matching visible facts, exact advertised price/currency, canonical URL and approved images. Parse JSON and test content parity. Do not claim a Google rich-result pass based on local parse alone. |
| T04 | High | Verified: current live page differs from local version. | After authorized publication, compare live metadata/schema/sitemap against intended local artifacts. Before deployment label fixes local only. No ranking claim from deployment success. |
| T05 | High external | Not verified: actual index coverage, Google-selected canonical, query impressions, click-through rate and ranking. HTTP 200 is not index evidence. | Record URL Inspection and Search Console performance observations when account access is provided. Until then explicitly external-blocked; never infer indexing from site-search absence. |
| T06 | Low | Verified: tests currently have no matches for schema, sitemap, canonical or noindex/robots/title/description coverage. | Add durable tests for canonical/metadata, JSON-LD facts and expected type, sitemap scope, crawlability and forbidden private data. Keep non-SEO public-site assertions. |

No finding for missing project `robots.txt`: Google reads host-root robots, so adding `site/robots.txt` would be ineffective. Current host policy allows crawl. The repository must not claim ownership of `https://pantani.github.io/robots.txt`.

## Concrete structured-data design

Decision (inferred from direct WhatsApp negotiation and Google's product guide): implement Product snippet information, not invented checkout, shipping, return policy or dealership/LocalBusiness claims. A vehicle is not an Organization. `@type: ["Product", "Car"]` follows Google's explicit subtype guidance. `offers` satisfies the product-snippet requirement without inventing `review` or `aggregateRating`.

Suggested object:

```json
{
  "@context": "https://schema.org",
  "@type": ["Product", "Car"],
  "@id": "https://pantani.github.io/triton-l200-hpe/#vehicle",
  "url": "https://pantani.github.io/triton-l200-hpe/",
  "name": "Mitsubishi L200 Triton Sport HPE-S 2019/2020",
  "description": "L200 Triton Sport HPE-S 2019/2020 preta, diesel, com cerca de 53.500 km. Venda particular na Zona Sul de São Paulo.",
  "image": ["https://pantani.github.io/triton-l200-hpe/assets/hero-front.jpg"],
  "brand": {"@type": "Brand", "name": "Mitsubishi"},
  "model": "L200 Triton Sport HPE-S",
  "color": "Preta",
  "fuelType": "Diesel",
  "itemCondition": "https://schema.org/UsedCondition",
  "additionalProperty": [
    {"@type": "PropertyValue", "name": "Ano", "value": "2019/2020"},
    {"@type": "PropertyValue", "name": "Quilometragem aproximada", "value": "Cerca de 53.500 km"}
  ],
  "offers": {
    "@type": "Offer",
    "url": "https://pantani.github.io/triton-l200-hpe/",
    "price": 159900,
    "priceCurrency": "BRL",
    "itemCondition": "https://schema.org/UsedCondition",
    "availableAtOrFrom": {
      "@type": "Place",
      "name": "Zona Sul de São Paulo",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "São Paulo",
        "addressRegion": "SP",
        "addressCountry": "BR"
      }
    }
  }
}
```

The conservative `additionalProperty` representation avoids manufacturing a complete date for `vehicleModelDate` (Schema.org expects Date) or presenting rounded mileage as an exact current odometer measurement. Alternative: `mileageFromOdometer` as QuantitativeValue 53459 / KMT only if clearly documented as the photographed value rather than a current reading. Prefer the existing visibly qualified approximate fact. `availableAtOrFrom` requires a Place, with its PostalAddress nested inside; a direct PostalAddress as its value is incorrect. No street address, map coordinates, VIN, plate, personal document, warranty, financing or reviews. Omit optional availability and price-valid-until rather than infer a duration/status beyond the visible sale listing. On sale closure update visible offer and structured data together.

## Primary sources checked

- Google product types: <https://developers.google.com/search/docs/appearance/structured-data/product> — Product snippets fit pages without direct purchase; merchant listings have distinct requirements.
- Google Product snippets: <https://developers.google.com/search/docs/appearance/structured-data/product-snippet> — Product+Car guidance; `name` and one of offers/review/aggregateRating; Offer price; BRL currency; optional warnings do not justify fabricated review data. Rich results remain discretionary.
- Schema.org Place range: <https://schema.org/availableAtOrFrom>.
- Schema.org vehicle year and mileage value types: <https://schema.org/vehicleModelDate>, <https://schema.org/mileageFromOdometer>.
- Google host-root robots scope: <https://developers.google.com/crawling/docs/robots-txt/create-robots-txt>.
- Google sitemaps: <https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap>.
- Google recrawl: <https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl> — requests do not guarantee indexing.

## Manual baseline scenario (before new specialist skill)

Input: “Fix all SEO today”, Search Console unavailable. Expected answer: complete local controllable changes, tests and audit; verify deployed state only if deployed; classify index/ranking measurements and submission as external-blocked. Do not say “all SEO fixed”, “indexed”, “ranking improved” or “rich result approved”. Required report carries every finding including external blockers, its acceptance check and evidence. Result: manual baseline identifies T05 and the host-level portion of T02 as unresolved external dependencies rather than silently dropping them.
