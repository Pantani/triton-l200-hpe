# Search Console evidence and indexing request

- Producer: orchestrator
- Consumer: final reviewer and site owner
- Completion: verified-live; indexing-request-accepted; actual indexing pending
- Date: 2026-10-03, America/Sao_Paulo
- Surface: existing signed-in Google Search Console session, browser UI
- Exact URL: `https://pantani.github.io/triton-l200-hpe/`

## Access discovery

Opening a dedicated project URL-prefix property showed no access. The existing
property selector exposed the root property `https://pantani.github.io/`, which
opened successfully and allowed inspection of the project URL. No new property,
credentials, access permissions, or ownership verification were created.
Earlier reports' absent-access assumptions are superseded by this observation.

## Actual index evidence

URL Inspection returned:

- `URL is not on Google`.
- `Page is not indexed: URL is unknown to Google`.
- No referring sitemap or referring page detected.
- Last crawl, fetch, user-declared canonical and Google-selected canonical: N/A.

This is direct index evidence, unlike a public `site:` query or HTTP 200. It
does not establish historical query volume or future ranking.

## Live test and action

The live URL test returned `URL is available to Google` and `Page can be indexed`.
The published version at the time had no structured enhancements. The
coordinator clicked Request indexing as part of the requested prior-audit
remediation. Google returned `Indexing requested` and confirmed the URL was added
to a priority crawl queue. No interactive CAPTCHA challenge was solved.

Screenshot evidence was saved outside the public artifact to
`/tmp/l200-indexing-requested.jpg` and copied to the chat visualization directory.
Do not publish account screenshots to the repository or website.

## Remaining acceptance

The request concerns the current public URL, not proof that uncommitted SEO
changes are deployed. The local sitemap still needs publication before
submission. Do not repeatedly request indexing; the confirmation explicitly
says repeat submissions do not change queue position or priority. Later inspect
actual index inclusion, Google-selected canonical, and page-filtered performance.
No indexing date, ranking gain, impressions, or field metrics are promised.

## Official Rich Results Test of candidate code

The coordinator submitted only the intended public `site/index.html` content
through the official tool's CODE tab. This checks the proposed schema without
claiming that it is already published. Result:

- **1 valid item detected**, under **Product snippets**.
- Item: Mitsubishi L200 Triton Sport HPE-S 2019/2020.
- Three non-critical optional-field warnings: `aggregateRating`, `review`, and
  Offer `availability`. The first two must not be fabricated; the third is
  deliberately omitted rather than treating an unverified current inventory
  state as a certified fact. None is a critical schema error.

Result URL:
https://search.google.com/test/rich-results/result?id=qDj8ifmJRR_rUpgfCBAhiw

This test consumed the same JSON-LD as the final candidate; subsequent hero
source/font-size repairs did not change structured data. A screenshot is kept
in the chat visualization directory, outside the repository. Eligibility in a
code test is not proof of deployed enhancement detection or actual display.

## Later host migration invalidates current-availability inference

At final public read-back (03:39 UTC), the original URL started returning HTTP301
to `http://pantani.xyz/triton-l200-hpe/`; following it failed DNS resolution. This
external change occurred after the successful live test/index request. Preserve
the successful request as historical evidence only. Confirm the intended domain,
DNS and TLS, then revisit canonical URLs and the correct Search Console property
before claiming current public availability. No repeated request was submitted.
