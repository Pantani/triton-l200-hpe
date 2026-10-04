"""Check the exact files that may be published by GitHub Pages."""

from pathlib import Path
import re
import unittest

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
HTML = SITE / "index.html"
WORKFLOW = ROOT / ".github" / "workflows" / "pages.yml"


class PublicSiteTests(unittest.TestCase):
    def read_html(self):
        self.assertTrue(HTML.is_file(), "site/index.html is missing")
        return HTML.read_text(encoding="utf-8")

    def test_required_vehicle_facts_are_visible(self):
        html = self.read_html()
        for fact in ("HPE-S", "2019/2020", "53,5 mil km", "R$ 150.000"):
            with self.subTest(fact=fact):
                self.assertIn(fact, html)
        self.assertEqual(len(re.findall(r"<h1\b", html)), 1)
        self.assertNotIn("R$ 159.900", html)

    def test_whatsapp_contact_is_direct(self):
        html = self.read_html()
        self.assertIn("https://wa.me/5511983587422", html)
        self.assertGreaterEqual(html.count("https://wa.me/5511983587422"), 2)

    def test_public_text_has_no_private_identifiers(self):
        html = self.read_html()
        self.assertNotRegex(html, r"\b[A-Z]{3}[0-9][A-Z0-9][0-9]{2}\b")
        self.assertNotRegex(html, r"\b[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}\b")
        for forbidden in ("RENAVAM", "CRLV-e", "R$ 153.000", "R$ 158.000"):
            self.assertNotIn(forbidden, html)

    def test_public_directory_has_no_source_documents(self):
        forbidden = {".pdf", ".heic"}
        self.assertFalse([p for p in SITE.rglob("*") if p.suffix.lower() in forbidden])

    def test_every_local_image_reference_exists_and_has_alt_text(self):
        html = self.read_html()
        images = re.findall(r"<img\b[^>]*>", html)
        self.assertGreaterEqual(len(images), 8)
        for image in images:
            with self.subTest(image=image[:80]):
                self.assertRegex(image, r'\balt="[^"]+"')
                src = re.search(r'\bsrc="(assets/[^"]+)"', image)
                self.assertIsNotNone(src)
                self.assertTrue((SITE / src.group(1)).is_file())

    def test_public_jpegs_keep_only_display_orientation(self):
        for image in SITE.rglob("*.jpg"):
            with self.subTest(image=image.name):
                with Image.open(image) as photo:
                    exif = photo.getexif()
                    self.assertLessEqual(set(exif), {274})
                    self.assertIn(exif.get(274, 1), (1, 6))

    def test_workflow_uploads_only_site_directory(self):
        self.assertTrue(WORKFLOW.is_file(), "Pages workflow is missing")
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("path: site/", workflow)
        self.assertNotIn("path: .\n", workflow)


if __name__ == "__main__":
    unittest.main()
