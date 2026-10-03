"""Protect photo orientation and privacy when generating web derivatives."""

from pathlib import Path
import re
from tempfile import TemporaryDirectory
import unittest

from PIL import Image

from tools.prepare_responsive_images import render_mobile_hero, render_variants


class ResponsiveImageTests(unittest.TestCase):
    def test_mobile_crop_keeps_oriented_height_center_and_privacy(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "hero.jpg"
            photo = Image.new("RGB", (600, 1200), "red")
            photo.paste("navy", (0, 200, 600, 1000))
            exif = Image.Exif()
            exif[274] = 6
            exif[315] = "Private fixture author"
            photo.save(source, exif=exif)
            original = source.read_bytes()
            path = render_mobile_hero(source, root / "output")
            self.assertEqual(source.read_bytes(), original)
            with Image.open(path) as result:
                self.assertEqual(result.size, (800, 600))
                self.assertEqual(dict(result.getexif()), {})
                self.assertNotIn("xmp", result.info)
                self.assertNotIn("icc_profile", result.info)
                red, _, blue = result.getpixel((400, 300))
                self.assertGreater(blue, red + 50)

    def test_mobile_crop_rejects_upscaling(self):
        with TemporaryDirectory() as directory:
            source = Path(directory) / "small.jpg"
            Image.new("RGB", (400, 600)).save(source)
            with self.assertRaises(ValueError):
                render_mobile_hero(source, Path(directory))

    def test_gallery_covers_all_approved_public_photos(self):
        site = Path(__file__).resolve().parents[1] / "site"
        html = (site / "index.html").read_text(encoding="utf-8")
        gallery = re.search(r'<div class="gallery">(.*?)</div>', html, re.DOTALL)
        self.assertIsNotNone(gallery)
        sources = set(re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', gallery.group(1)))
        approved = {f"assets/{photo.name}" for photo in (site / "assets").glob("*.jpg")}
        self.assertTrue(approved)
        self.assertEqual(sources, approved)

    def test_derivatives_preserve_display_orientation_without_metadata(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.jpg"
            photo = Image.new("RGB", (1200, 800), "navy")
            exif = Image.Exif()
            exif[274] = 6
            exif[315] = "Private fixture author"
            photo.save(source, exif=exif)
            original = source.read_bytes()
            paths = render_variants(source, root / "output")
            self.assertEqual(source.read_bytes(), original)
            self.assertEqual(len(paths), 2)
            for path in paths:
                with self.subTest(path=path), Image.open(path) as result:
                    self.assertEqual(result.height, result.width * 3 // 2)
                    self.assertEqual(dict(result.getexif()), {})
                    self.assertNotIn("xmp", result.info)

    def test_small_sources_are_not_upscaled(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "small.jpg"
            Image.new("RGB", (200, 100), "black").save(source)
            paths = render_variants(source, root / "output")
            self.assertEqual([path.name for path in paths], ["small-full.webp"])
            with Image.open(paths[0]) as result:
                self.assertEqual(result.size, (200, 100))

    def test_missing_source_does_not_report_success(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(FileNotFoundError):
                render_variants(root / "missing.jpg", root / "output")


if __name__ == "__main__":
    unittest.main()
