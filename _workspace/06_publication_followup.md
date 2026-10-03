# Publication and domain follow-up

- Producer: coordinator
- Consumer: owner and future SEO operators
- Date: 2026-10-03
- State: deployed and verified; index inclusion and sitemap processing external-pending
- Authorization: owner approved the five follow-up recommendations with `seguir`.
- Base: `e1a4465`; pre-existing photo deletion and rewritten history preserved.

## Superseding finding dispositions

| Finding | Current evidence | State / residual |
| --- | --- | --- |
| E01 / F01 domain migration | DNS/TLS works. Local canonical, OG, Product/Car/Offer and sitemap use HTTPS pantani.xyz. | verified-live after deployment |
| T02 discovery | Host-root robots and sitemap fixed in separate hosting repository, commit `1231f02`, successful Pages run 37102726689. Both public files read back with corrected HTTPS domain; robots advertises listing sitemap. | verified-live at host root and listing; submission accepted; Google live fetch successful; processing pending |
| T01/C01/C02/C03/C04 regional copy | Reviewed truthful São Paulo title, H1, description, location and statewide visit information retained. HPE-S stays the actual variant. | verified-live |
| T03/T06 schema and invariants | 21 tests pass, including new-domain canonical/social/sitemap agreement and public-photo privacy. | verified-live; Google live test detected one valid Product snippet |
| T04/C05/DEPLOY-01/F02/F03/F05 | Full site assets, fonts, sitemap, tools, tests and requested harness prepared together. | verified-live |
| PERF-01/R01 | Mobile hero retains full 1053-pixel height while cropping sides outside the portrait display. 403,222 to 215,360 bytes; full desktop image and all 17 JPEG originals retained. | verified-live; public lab baseline99 performance/LCP2.250s; field performance unmeasured |
| R02 responsive rendering | Parent browser checked widths 320,390,412,480,700,1440 with no horizontal overflow. Crop selected only through480 portrait; full image selected in700 landscape and1440 desktop. Visual screenshots390/480 preserve detail and contact access. | verified-local |
| R03/R04/F04 privacy/fonts | Approved JPEG bytes unchanged; 52 metadata-free WebPs; self-hosted original fonts/licenses. Pages artifact remains only site/. | verified-local |
| T05 indexing | New domain Search Console property accessible; Performance still processing, no established traffic baseline. | Google live test successful; index request accepted; actual inclusion/ranking unmeasured |
| M01 contact measurement | No analytics collector/ID configured. Owner asked for existing service/property. Manual Search Console measurement procedure documented. | owner-input pending; no tracking claim |
| C06 extra vehicle facts | Owner asked to confirm gearbox/drivetrain and service evidence. | owner-input pending; omitted rather than guessed |

## Decisions

The user-approved domain is the actual HTTPS destination already served by
GitHub Pages. No new hosting provider or frontend runtime was introduced.
Root discovery required two narrowly scoped edits in the portfolio hosting repo;
its visible portfolio content was not changed.

Explicit hero preload showed no meaningful simulated LCP benefit; inlining all
CSS offered little LCP improvement and increased source maintenance. Both were
discarded. The mobile crop preserves height/detail rather than restoring the
previous blurry reduced-resolution source. Its aspect ratio must be reviewed
again if hero content/layout changes. The measured residual is not hidden.

The site still has no analytics script: a fake ID, browser-local counter, or
unconfigured event hook would not establish aggregate click measurement.
`docs/harness/seo/measurement.md` records configuration and validation requirements.

## Verification

Coordinator: 21 tests passed with the existing pinned Pillow environment;
authored-file git diff --check passed; all 17 source JPEGs byte-identical to HEAD. Independent
technical review is in 05_technical_followup.md. Independent performance review
and exact Lighthouse results are in 05_performance_followup.md.

The staged full-tree whitespace check flagged only upstream OFL license files
(original CRLF/trailing spaces). Those three vendor license texts are retained
byte-for-byte intentionally; the check passes with only `*-OFL.txt` excluded.
No application-source whitespace warning was suppressed.

## Published evidence

Listing commit `14c91aa`; Pages run 37103048725 completed successfully, including
all21 tests. Read-back of HTML, sitemap, styles.css, fonts.css, mobile hero and
heading WOFF2 returned200 and byte-for-byte equality with the candidate. Old
HTTPS github.io URL returns301 to the new HTTPS page. No X-Robots-Tag was added.
Browser read-back confirmed the new canonical and mobile source.

The Google Search Console domain property `sc-domain:pantani.xyz` is accessible.
The new URL was unknown/not indexed when inspected. The live test succeeded at
03:28 local time: URL available to Google, page can be indexed, one valid Product
snippet with non-critical issues. Indexing request accepted into a priority
crawl queue. No interactive CAPTCHA challenge was solved. No repeated index
requests were made for this new URL.

Sitemap submission returned a success modal, but its report initially showed
Couldn't fetch. Public HTTPS fetch and XML parse both pass, including a request
with Googlebot user-agent (which does not impersonate Google's network).
Following Google's documented troubleshooting, the sitemap URL itself was
Live-tested at03:30:30localtime: CrawlallowedYes, PagefetchSuccessful,
IndexingallowedYes. This establishes current Google Inspection Tool access,
not success of the separate sitemap-processing report. Initial failure cause
remains unverified; no server or XML defect was reproduced. Processing remains
external-pending, and Google documents automatic retries for several days.

Sources: https://support.google.com/webmasters/answer/7451001

Screenshots are saved outside the repository in the task visualization folder.


## Public performance baseline

One public mobile Lighthouse13.5.0 run at06:28:47UTC returned performance99,
accessibility100, best-practices100, automatedSEO100, simulatedLCP2.250s,
FCP0.943s, TBT0, CLS0.00262 and1,517,229bytes. The coordinator independently
read the JSON report. This is a separate deployed baseline, not a causal
comparison against Python localhost. No real-user Core Web Vitals or ranking
improvement was established. Full evidence: 05_performance_followup.md.
