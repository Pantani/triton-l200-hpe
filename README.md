# L200 Triton Sport HPE-S private-sale site

This repository contains a static, single-page listing for a Mitsubishi L200 Triton Sport HPE-S 2019/2020. GitHub Pages publishes only the `site/` directory through `.github/workflows/pages.yml`.

## Local preview

```sh
python3 -m http.server 8000 --directory site
```

Open `http://localhost:8000/` to review the page. No frontend build step is needed.

## Verification

Install the test dependency and run the public-site checks:

```sh
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
```

The checks validate key facts, contact links, the Pages artifact boundary, image references, and JPEG metadata. Final image pixels and page layouts must also be reviewed visually before publishing.

## Photos and privacy

The current repository tree keeps only the 17 privacy-reviewed JPEG photos in `site/assets/`. The original HEIC photos and the source-photo export script were removed. No image pixels were rotated during preparation; the approved JPEGs retain only the EXIF display-orientation tag where required.

Six JPEGs required manual privacy edits to hide a house number, vehicle plates or bystanders, an identifying tattoo, or third-party contact details. Generative edits can affect pixels beyond the requested area, so review each approved photo visually before reusing it.

The root `CRLV-e.pdf` is ignored by Git and is never included in the Pages artifact. Do not copy documents, plate identifiers, personal details, or private negotiation terms into `site/`. The repository itself is public, including its existing Git history; limiting the Pages artifact does not rewrite that history.

## Publishing

Push updates to `main`. The workflow verifies the site, uploads `site/`, and deploys it to GitHub Pages at <https://pantani.github.io/triton-l200-hpe/>.
