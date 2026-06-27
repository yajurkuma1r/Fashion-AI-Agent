from pathlib import Path
from PIL import Image


def save_image(
    image: Image.Image,
    output_dir: Path,
    filename: str,
) -> Path:
    """
    Saves a PIL image to disk.

    Args:
        image: PIL Image object.
        output_dir: Directory where image should be saved.
        filename: Output filename.

    Returns:
        Path to the saved image.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / filename

    image.save(
        output_path,
        format="PNG",
        optimize=True,
    )

    return output_path