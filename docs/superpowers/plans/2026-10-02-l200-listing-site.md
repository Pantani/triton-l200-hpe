# L200 Listing Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a factual, mobile-friendly private-sale site for the owner's L200 on GitHub Pages.

**Architecture:** A static `site/` directory holds HTML, CSS, and prepared JPEG assets. A GitHub Actions workflow uploads only this directory to Pages. Python `unittest` checks with Pillow inspect the exact public directory before deployment.

**Tech Stack:** HTML5, CSS, Python `unittest` and Pillow, GitHub Actions/Pages. No JavaScript runtime or frontend build dependency.

**Spec:** `docs/superpowers/specs/2026-10-02-l200-listing-site-design.md`

## Global Constraints

- Public copy is in Brazilian Portuguese; code, comments, README, and workflow labels are in English.
- Use only the owner-confirmed vehicle facts, R$ 159.900 asking price, and confirmed public WhatsApp number.
- Do not publish CRLV, plate text, personal identifiers, exact address, negotiation range, or unconfirmed vehicle claims.
- Do not rotate any photo or apply automatic orientation normalization. Exclude an image if its browser rendering is sideways.
- Prepare selected images as separate public assets; inspect final pixels and strip metadata.
- Preserve the owner's local photo deletions; do not restore removed originals.

---

## File structure

- `site/index.html`: complete page content, social metadata, native gallery links, and WhatsApp actions.
- `site/styles.css`: responsive presentation and keyboard focus styling.
- `site/assets/*.jpg`: selected, resized, privacy-reviewed photographs.
- `site/favicon.svg`: small vehicle-themed mark without third-party logos.
- `tests/test_site.py`: public directory privacy/content/asset contract.
- `.github/workflows/pages.yml`: checks and deploys only `site/`.
- `README.md`: editing and local verification instructions.

## Task 1: Curated source and public asset checks

**Files:** Modify `photos/` tracking to match the owner's existing deletions; create `tests/test_site.py`; create `site/assets/*.jpg`.

**Interfaces:** Tests read `site/` directly. Later page code references only assets that pass these checks.

- [ ] **Step 1: Preserve the owner's curation.** Confirm the 17 current HEIC paths and stage only the files the owner deleted. Commit their deletions without restoring or altering remaining sources.
- [ ] **Step 2: Start a worktree** at the resulting local commit; keep implementation changes isolated from `main`.
- [ ] **Step 3: Write failing tests** for public asset boundaries and privacy. The tests require `site/index.html`, reject `.pdf`/`.heic` in `site/`, allow only the EXIF display-orientation tag in public JPEGs, require every local image reference to resolve, and reject a license-plate-shaped token in public text.

```python
def test_public_directory_has_no_source_documents(self):
    forbidden = {".pdf", ".heic"}
    self.assertFalse([p for p in SITE.rglob("*") if p.suffix.lower() in forbidden])

def test_public_jpegs_keep_only_display_orientation(self):
    for image in SITE.rglob("*.jpg"):
        with Image.open(image) as photo:
            self.assertLessEqual(set(photo.getexif()), {274})
```

- [ ] **Step 4: Run** `rtk proxy python3 -m unittest discover -s tests -v`; confirm a failing test because `site/index.html` does not yet exist.
- [ ] **Step 5: Export the exact selected gallery** from the spec into `site/assets/`. For each candidate, keep source orientation, produce a web-sized JPEG, remove metadata except the display-orientation tag, and inspect the resulting pixels. Apply deterministic plate masks and crops for the specific privacy details listed in the spec; compare the result with the source to ensure the vehicle remains faithful and unrotated. Skip any image that cannot satisfy privacy, fidelity, and orientation constraints.
- [ ] **Step 6: Re-run the asset/privacy tests** and inspect every delivered image at its final size.

## Task 2: Page structure and visual design

**Files:** Create `site/index.html`, `site/styles.css`, `site/favicon.svg`, `README.md`; extend `tests/test_site.py`.

**Interfaces:** `index.html` references `assets/...` paths relative to the project URL. Native image links provide enlarged viewing; no JavaScript is required.

- [ ] **Step 1: Add failing content tests** for one H1, asking price, approximate mileage, WhatsApp links, required alt text, and absent unconfirmed claims.

```python
def test_public_copy_contains_asking_price_and_mileage(self):
    html = (SITE / "index.html").read_text(encoding="utf-8")
    self.assertIn("R$ 159.900", html)
    self.assertIn("53,5 mil km", html)
    self.assertIn("HPE-S", html)
```

- [ ] **Step 2: Run the tests and confirm they fail** for missing content.
- [ ] **Step 3: Implement semantic HTML** in the spec's page order: header, hero, highlights, gallery, specifications, owner statements, FAQ, and contact. Use `https://wa.me/5511983587422` with a URL-encoded prefilled message. Keep the visible number out of unrelated metadata.
- [ ] **Step 4: Implement CSS** with a mobile-first layout, large real images, off-white/graphite/bronze palette, readable body text, clear focus states, and responsive gallery. Use system fonts and no remote dependencies.
- [ ] **Step 5: Add metadata and favicon** using the verified project-site URL. Use only owner-provided facts in social copy.
- [ ] **Step 6: Run tests** and visually review at narrow and wide viewport sizes; correct any overflow, awkward crops, or unreadable sections.

## Task 3: Pages deployment and final verification

**Files:** Create `.github/workflows/pages.yml`; update `README.md`.

**Interfaces:** The workflow packages `site/` only, after `python3 -m unittest discover -s tests -v` passes.

- [ ] **Step 1: Add workflow validation** that reads the YAML and confirms the artifact upload path is `site/`, not repository root.
- [ ] **Step 2: Run the test and confirm it fails** because the workflow is absent.
- [ ] **Step 3: Add a Pages workflow** using the official `actions/checkout@v5`, `actions/configure-pages@v5`, `actions/upload-pages-artifact@v4`, and `actions/deploy-pages@v4` pattern. Give the deploy job `pages: write` and `id-token: write`, and upload `path: site/`.
- [ ] **Step 4: Run all tests and a public-file review**. Verify no document or HEIC is in `site/`, no plate/address/contact details appear in final pixels, no image is rotated, and all links/assets load locally.
- [ ] **Step 5: Commit, push, enable GitHub Pages Actions source if needed, and verify** the deployed URL, TLS, hero image, mobile layout, WhatsApp action, and workflow status. Record the final URL in `README.md`.

Official workflow reference: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
