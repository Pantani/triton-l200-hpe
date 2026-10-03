"""Build smaller web assets from approved public JPEGs, never source photos."""

from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "site" / "assets"


def variant_widths(width):
    """Use small display sizes plus the original width without upscaling."""
    return [size for size in (480, 960) if size < width] + [width]


def save_variant(image, source, output, width):
    """Save oriented pixels without inherited EXIF, ICC, or XMP payloads."""
    suffix = str(width) if width < image.width else "full"
    destination = output / f"{source.stem}-{suffix}.webp"
    height = round(image.height * width / image.width)
    resized = image.resize((width, height), Image.Resampling.LANCZOS)
    resized.info.clear()
    resized.save(destination, "WEBP", quality=82, method=6)
    return destination


def render_variants(source, output):
    """Keep the approved source unchanged and bake its display orientation."""
    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
    output.mkdir(parents=True, exist_ok=True)
    return [save_variant(image, source, output, width)
            for width in variant_widths(image.width)]


def render_mobile_hero(source, output):
    """Omit off-screen sides while keeping the portrait hero's full pixel height."""
    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
    if image.width < 800:
        raise ValueError("Mobile hero needs at least 800 oriented source pixels")
    left = (image.width - 800) // 2
    cropped = image.crop((left, 0, left + 800, image.height))
    cropped.info.clear()
    output.mkdir(parents=True, exist_ok=True)
    destination = output / "hero-front-mobile.webp"
    cropped.save(destination, "WEBP", quality=82, method=6)
    return destination


def main():
    output = ASSETS / "responsive"
    sources = sorted(ASSETS.glob("*.jpg"))
    if not sources:
        raise SystemExit("No approved public JPEGs found in site/assets")
    for source in sources:
        paths = render_variants(source, output)
        print(f"{source.name}: {len(paths)} responsive WebP variants")
    render_mobile_hero(ASSETS / "hero-front.jpg", output)


if __name__ == "__main__":
    main()
