import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)


def generate_fashion_model(image_path: Path, prompt: str):
    """
    Generates an AI fashion model wearing the uploaded outfit.

    Args:
        image_path: Path to the clothing image.
        prompt: Prompt describing the desired output.

    Returns:
        Raw OpenAI response.
    """

    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    with open(image_path, "rb") as image_file:
        response = client.images.edit(
            model="gpt-image-1",
            image=image_file,
            prompt=prompt,
        )

    return response