"""Export faithful, privacy-reviewed JPEGs from the owner's selected HEICs."""

from dataclasses import dataclass
from pathlib import Path
import subprocess
import tempfile

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "photos"
DESTINATION = ROOT / "site" / "assets"
PREVIEW_SIZE = (1200, 900)
PLATE_FILL = (210, 213, 216)


@dataclass(frozen=True)
class Photo:
    source: str
    output: str
    crop: tuple[int, int, int, int] | None = None
    masks: tuple[tuple[int, int, int, int], ...] = ()


PHOTOS = (
    Photo("IMG_6686.HEIC", "hero-front.jpg", (0, 80, 1090, 870), ((145, 460, 255, 550),)),
    Photo("IMG_6679.HEIC", "side-profile.jpg", (0, 285, 1200, 780)),
    Photo("IMG_6682.HEIC", "rear-three-quarter.jpg", (160, 195, 1200, 850), ((975, 575, 1075, 645),)),
    Photo("IMG_6699.HEIC", "rear-seats.jpg"),
    Photo("IMG_6626.HEIC", "odometer.jpg"),
    Photo("IMG_6644.HEIC", "all-terrain-tread.jpg"),
    Photo("IMG_6645.HEIC", "all-terrain-sidewall.jpg"),
    Photo("IMG_6697.HEIC", "jbl-head-unit.jpg", (0, 0, 685, 900)),
    Photo("IMG_6628.HEIC", "active-subwoofer.jpg"),
    Photo("IMG_6625.HEIC", "shiftpower.jpg"),
    Photo("IMG_6702.HEIC", "covered-bed.jpg"),
)


def scaled_box(box: tuple[int, int, int, int], image: Image.Image) -> tuple[int, int, int, int]:
    x_scale = image.width / PREVIEW_SIZE[0]
    y_scale = image.height / PREVIEW_SIZE[1]
    left, top, right, bottom = box
    return (round(left * x_scale), round(top * y_scale), round(right * x_scale), round(bottom * y_scale))


def convert_heic(source: Path, destination: Path) -> None:
    result = subprocess.run(
        ["sips", "-s", "format", "jpeg", "-Z", "1600", "-o", str(destination), str(source)],
        check=True,
        capture_output=True,
        text=True,
    )
    if not destination.is_file():
        raise RuntimeError(f"Could not convert {source.name}: {result.stdout}{result.stderr}")


def save_photo(photo: Photo, temporary: Path) -> None:
    convert_heic(SOURCE / photo.source, temporary)
    with Image.open(temporary) as source:
        orientation = source.getexif().get(274, 1)
        image = source.convert("RGB")
    if orientation not in (1, 6):
        raise ValueError(f"Unsupported orientation for {photo.source}: {orientation}")

    draw = ImageDraw.Draw(image)
    for mask in photo.masks:
        draw.rectangle(scaled_box(mask, image), fill=PLATE_FILL)
    if photo.crop:
        image = image.crop(scaled_box(photo.crop, image))

    public_exif = Image.Exif()
    public_exif[274] = orientation
    image.save(
        DESTINATION / photo.output,
        "JPEG",
        quality=84,
        optimize=True,
        progressive=True,
        exif=public_exif,
    )


def main() -> None:
    DESTINATION.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="l200-photo-export-") as directory:
        temporary = Path(directory)
        for photo in PHOTOS:
            save_photo(photo, temporary / f"{photo.output}.jpg")


if __name__ == "__main__":
    main()
