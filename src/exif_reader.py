from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def decode_gps_info(gps_info):
    decoded = {}
    for key, value in gps_info.items():
        name = GPSTAGS.get(key, key)
        decoded[name] = value
    return decoded


def read_exif(image_path):
    path = Path(image_path)

    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    with Image.open(path) as image:
        raw_exif = image.getexif()

        if not raw_exif:
            return {
                "file": str(path),
                "has_exif": False,
                "has_gps": False,
                "metadata": {},
                "message": "No EXIF metadata found."
            }

        metadata = {}

        for tag_id, value in raw_exif.items():
            tag_name = TAGS.get(tag_id, tag_id)

            if tag_name == "GPSInfo":
                metadata["GPSInfo"] = decode_gps_info(value)
            else:
                metadata[tag_name] = value

        return {
            "file": str(path),
            "has_exif": True,
            "has_gps": "GPSInfo" in metadata,
            "metadata": metadata,
            "message": "EXIF metadata found."
        }


def print_summary(result):
    print(f"File: {result['file']}")
    print(f"Has EXIF: {result['has_exif']}")
    print(f"Has GPS: {result['has_gps']}")
    print(f"Message: {result['message']}")

    if result["metadata"]:
        print("\nMetadata:")
        for key, value in result["metadata"].items():
            print(f"- {key}: {value}")


if __name__ == "__main__":
    image_path = input("Enter image path: ").strip()
    result = read_exif(image_path)
    print_summary(result)
