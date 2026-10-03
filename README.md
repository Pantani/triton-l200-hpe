# L200 Triton Sport HPE-S private-sale site

This repository contains a static, single-page listing for a Mitsubishi L200 Triton Sport HPE-S 2019/2020. GitHub Pages publishes only the `site/` directory through `.github/workflows/pages.yml`.

## Local preview

```sh
python3 -m http.server 8000 --directory site
```

Open `http://localhost:8000/` to review the page. No frontend build step is needed.

## Verification

Install the test dependency in an isolated environment and run the public-site checks:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
```

The checks validate key facts, contact links, the Pages artifact boundary, image references, metadata privacy, canonical/sitemap agreement, and structured offer consistency. Final image pixels and page layouts must also be reviewed visually before publishing.

## Photos and privacy

The current repository tree keeps only the 17 privacy-reviewed JPEG photos in `site/assets/`. The original HEIC photos and the source-photo export script were removed. No image pixels were rotated during preparation; the approved JPEGs retain only the EXIF display-orientation tag where required.

Six JPEGs required manual privacy edits to hide a house number, vehicle plates or bystanders, an identifying tattoo, or third-party contact details. Generative edits can affect pixels beyond the requested area, so review each approved photo visually before reusing it.

The root `CRLV-e.pdf` is ignored by Git and is never included in the Pages artifact. Do not copy documents, plate identifiers, personal details, or private negotiation terms into `site/`. The repository is public. Earlier commits still contain the original HEIC photos; deleting them from the current tree does not erase Git history.

### Responsive image assets

After changing an approved public JPEG, regenerate its responsive WebP assets:

```sh
python3 tools/prepare_responsive_images.py
python3 -m unittest discover -s tests -v
```

The generator reads only `site/assets/*.jpg`, applies their existing display
orientation, and writes metadata-free variants under `site/assets/responsive/`.
It does not overwrite JPEGs or read private HEIC sources. Full JPEG links remain
available for close inspection. Smaller WebP candidates trade additional static
storage for reduced browser transfer; inspect the result before publishing.

The hero also has an 800-pixel-wide central crop for portrait screens up to
480 CSS pixels. It keeps the source's full oriented height instead of scaling
down the details. Wider and landscape screens use the full image. Recheck the
hero's rendered aspect ratio after changing its content or layout; the crop is
only equivalent while the visible box is narrower than the cropped image ratio.

### Local fonts

The original Barlow Condensed, IBM Plex Sans and IBM Plex Mono typefaces are
served locally through `site/fonts.css`, preserving the design without a
render-blocking Google Fonts stylesheet request. Sources, hashes and unmodified
OFL licenses are retained in [the font provenance record](site/assets/fonts/SOURCES.md).

## SEO maintenance

Start with the [SEO orchestrator](.agents/skills/seo-orchestrator/SKILL.md) and
[team contract](docs/harness/seo/team-spec.md). The latest evidence and finding
dispositions are in [_workspace/04_seo_final_audit.md](_workspace/04_seo_final_audit.md).
Keep price, mileage, availability and location consistent between visible text
and JSON-LD. When the vehicle is sold, update both the visible listing and offer.
Do not fabricate reviews, delivery terms, dealerships or city-specific copies.

After publication, verify the canonical page and `sitemap.xml` return 200, then
inspect the URL in Google Search Console and submit the sitemap:
`https://pantani.xyz/triton-l200-hpe/sitemap.xml`.
The host-root `robots.txt` and root sitemap belong to another repository;
adding a robots file under this project path would not control crawling.

Use URL Inspection to check the Google-selected canonical and index status.
Request indexing after verifying the deployed page if appropriate. Validate
structured data with Google's Rich Results Test; local JSON checks do not prove
Google eligibility or actual rich-result display. Review query impressions,
clicks, CTR and average position for this exact page after enough data accrues.
Compare equal periods and distinguish lack of data from zero demand. No local
test or Lighthouse score guarantees indexing or ranking.
See [the measurement procedure](docs/harness/seo/measurement.md) for the exact
page filter, baseline limitations, and contact-event setup requirements.

## Publishing

Push updates to `main`. The workflow verifies the site, uploads `site/`, and deploys it to GitHub Pages at <https://pantani.xyz/triton-l200-hpe/>.
