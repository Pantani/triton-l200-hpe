# L200 Private-Sale Site Design

## Purpose and status

Build a one-page, mobile-first GitHub Pages site for the private sale of a black Mitsubishi L200 Triton Sport HPE-S 2019/2020. The page should let a buyer assess the vehicle quickly and contact the owner on the confirmed public WhatsApp number. This document defines the proposed site; implementation and publication follow review.

Before implementation, the repository had no website. It is public and its Git history contains 84 HEIC originals in `photos/`. The owner curated that folder: 17 files remain and 67 deletions were committed before site work began. The root `CRLV-e.pdf` is local and ignored by Git. GitHub Pages had not been configured as of the initial design review on October 2, 2026 (the Pages API returned 404).

## Approach

Use a small static site in `site/`: semantic HTML and focused CSS. Native image links provide full-size viewing without JavaScript. A GitHub Actions workflow should upload **only `site/`** as the Pages artifact. The workflow gives the public website a clear publication boundary, independent of the rest of the repository. The source repository itself remains public; the existing `photos/` Git history is a separate privacy concern and this site does not erase it.

Alternatives considered:

1. Copy the apartment site's single large HTML file. This carries apartment-specific layout and copy and makes future edits harder, despite being quick to start.
2. Publish from `main`'s repository root or `/docs` folder. The root would include unrelated files; `/docs` would require moving this specification and other documentation outside the publishing directory. Both are simple, but the Actions artifact is a clearer content boundary here.
3. Add a React build. The page needs only one route and a small gallery, so dependencies and build tooling add maintenance without buyer-facing value.

The chosen approach keeps the apartment site's editorial hierarchy and direct owner contact, with a visual treatment suited to a black pickup: warm off-white background, graphite text, restrained bronze accent, large real photographs, readable specifications, and no dealership-style claims.

## Public facts and copy

Use these owner-provided facts as the sole source for public claims:

- Mitsubishi L200 Triton Sport HPE-S, 2019/2020, black, diesel, 2.4 turbo, 2,442 cm³, 190 cv, double cab, five seats.
- Approximately 53,500 km. The current odometer photo reads 53,459 km, so the headline can say `53,5 mil km` or `cerca de 53.500 km`; do not present the rounded figure as an exact photo reading.
- All revisions performed and current; well cared for; all-terrain tires practically new.
- Original factory JBL sound system, active subwoofer, and installed ShiftPower throttle-response controller. Explain ShiftPower as changing accelerator-pedal response; never claim extra engine power.
- No auction history and no sinistro, as confirmed by the owner. Trades are not accepted.
- Public asking price: **R$ 159.900**. Do not publish a private negotiation range or imply urgency from the owner's reason for sale.

Do not claim an owner count, dealership service, paid taxes/licensing, warranty, accident-free paint, no repaint, no off-road use, no towing, spare key, financing, or other unconfirmed detail. A buyer may ask for revision records and an in-person inspection, but the page must not show personal documents.

## Page flow

1. **Header:** model name, anchor links to photos/specifications/questions, and a WhatsApp action.
2. **Hero:** strongest approved three-quarter front photo, `L200 Triton Sport HPE-S 2019/2020`, `53,5 mil km`, `R$ 159.900`, concise private-sale framing, and a prominent WhatsApp action.
3. **Highlights:** low mileage, revisions current, nearly new all-terrain tires, JBL sound, subwoofer, ShiftPower. Use short factual labels.
4. **Photo gallery:** vehicle first, then interior/odometer, tires and accessories. Provide useful alt text and a keyboard-accessible enlarged view if implemented.
5. **Vehicle details:** a compact definition list or table for year, version, color, fuel, engine, displacement, power, body style, capacity, and mileage. Avoid unverified transmission/traction/equipment claims.
6. **Ownership notes:** revisions current, no auction history, no sinistro, no trades. Phrase these as owner statements, not a certified inspection.
7. **Questions and contact:** short answers to common buyer questions and a second WhatsApp action. Visit by arrangement; no street address or exact location on the page.

The page should remain useful with JavaScript disabled: essential copy, images, price, and WhatsApp links render in HTML. WhatsApp links use the number the owner confirmed for public use and a short prefilled inquiry message.

## Photos and privacy

Use only derived assets in `site/assets/`, not `photos/` HEIC originals. Resize and compress deterministically, retain only the EXIF display-orientation tag where needed, and inspect the final pixels. Do not rotate image pixels or apply automatic orientation normalization. Preserve vehicle appearance and the odometer reading. The exact frame and any redaction must be reviewed before an image is published.

### Revised gallery selection

| Order | Source | Purpose | Preparation before publishing |
| --- | --- | --- | --- |
| 1 | `IMG_6686.HEIC` | Front three-quarter cover | Mask the vehicle plate and crop surrounding street details. |
| 2 | `IMG_6679.HEIC` | Complete side profile | Crop the top of the frame to remove the visible building number. |
| 3 | `IMG_6682.HEIC` | Rear three-quarter view | Mask the vehicle plate and crop out the building number and the neighboring car's plate. |
| 4 | `IMG_6699.HEIC` | Rear-seat view | Use after metadata removal and final pixel inspection. |
| 5 | `IMG_6626.HEIC` | Odometer | Preserve the photographed 53,459 km reading. |
| 6 | `IMG_6644.HEIC` | Tire tread and wheel | Use after metadata removal. |
| 7 | `IMG_6645.HEIC` | Tire sidewall and wheel | Include for additional wheel and tire detail. |
| 8 | `IMG_6697.HEIC` | JBL head unit | Crop to remove third-party contact details. |
| 9 | `IMG_6628.HEIC` | Active subwoofer | Use after metadata removal. |
| 10 | `IMG_6625.HEIC` | ShiftPower control | Use after metadata removal. |

`IMG_6685.HEIC` was excluded because the tree and background plates weaken its composition and privacy. `IMG_6665.HEIC` exposes the building number; `IMG_6669.HEIC` and `IMG_6684.HEIC` show people and vehicle plates. `IMG_6690.HEIC` and `IMG_6702.HEIC` show a hand and do not improve the sales story. `IMG_6698.HEIC` is an interior-wide shot but has a prominent bag with third-party contact details. A new clean interior-wide shot and a clear photo of the open pickup bed would improve the page, but the site should not depend on them. These excluded files remain untouched.

Never publish the CRLV PDF, plate number, CPF, RENAVAM, complete VIN, QR code, security code, personal address, or document images. Exclude private negotiation numbers from all public files, metadata, and source comments. Check the final Pages artifact contents before deployment.

## Accessibility, search, and performance

Use responsive layout and typography; visible focus states; descriptive alt text; sufficient contrast; appropriately sized tap targets; and a gallery that works by keyboard. Keep image dimensions explicit to avoid layout jumps. Favor local assets and no third-party fonts, scripts, analytics, or tracking. Add a title, description, canonical URL, social preview image, and favicon after the Pages URL is confirmed. Avoid unsupported structured claims.

The project URL is expected to follow GitHub's project-site form, `https://pantani.github.io/triton-l200-hpe/`, but verify the actual deployment URL before placing it in canonical and social metadata.

## Delivery and verification

Implement `site/index.html`, `site/styles.css`, optional small `site/app.js`, selected optimized assets, an English README, and the Pages workflow. Check desktop and mobile rendering, all anchors and WhatsApp links, gallery keyboard use, original orientation and privacy of every delivered image, copy against the fact list, artifact contents, and the actual Pages URL. Publish only after those checks and review of the finished page. GitHub's official Pages documentation confirms a custom workflow can upload a selected directory with `actions/upload-pages-artifact` and deploy it with `actions/deploy-pages`.

Reference: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
