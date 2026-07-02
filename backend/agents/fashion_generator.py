from pathlib import Path

from backend.services.image_generation_service import (
    generate_fashion_model,
)
from backend.services.storage_service import save_image


class FashionGenerator:
    """
    Main AI Agent responsible for generating
    fashion model images.
    """

    def generate(
        self,
        image_path: Path,
        prompt: str,
        output_dir: Path,
        filename: str,
    ) -> Path:
        """
        Complete generation workflow.

        1. Generate AI model
        2. Save image
        3. Return saved image path
        """

        generated_image = generate_fashion_model(
            image_path=image_path,
            prompt=prompt,
        )

        saved_image = save_image(
            image=generated_image,
            output_dir=output_dir,
            filename=filename,
        )

        return saved_image