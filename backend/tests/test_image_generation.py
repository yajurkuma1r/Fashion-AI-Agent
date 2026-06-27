from pathlib import Path

from backend.services.image_generation_service import generate_fashion_model

prompt = Path(
    "backend/prompts/fashion_catalogue_prompt.txt"
).read_text(encoding="utf-8")

image_path = Path(
    "backend/tests/sample_images/real_test.jpeg"
)

generated_image = generate_fashion_model(
    image_path=image_path,
    prompt=prompt,
)

output_dir = Path("backend/output/generated")
output_dir.mkdir(parents=True, exist_ok=True)

output_path = output_dir / "fashion_model.png"

generated_image.save(output_path)

print(f"✅ Image saved to: {output_path}")