from pathlib import Path
import shutil
import uuid

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

from backend.agents.fashion_generator import FashionGenerator
from backend.services.instagram_service import InstagramService

app = FastAPI(
    title="Fashion AI Agent",
    version="1.0.0",
)

agent = FashionGenerator()
instagram = InstagramService()

UPLOAD_DIR = Path("backend/output/uploads")
GENERATED_DIR = Path("backend/output/generated")

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
GENERATED_DIR.mkdir(parents=True, exist_ok=True)


class ApproveRequest(BaseModel):
    filename: str


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "Fashion AI Agent",
    }


@app.post("/generate")
async def generate(file: UploadFile = File(...)):
    """
    Upload outfit image.
    Generate AI fashion model.
    """

    unique_name = f"{uuid.uuid4()}.png"

    uploaded_image = UPLOAD_DIR / unique_name

    with uploaded_image.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    prompt = Path(
        "backend/prompts/fashion_catalogue_prompt.txt"
    ).read_text(encoding="utf-8")

    generated_image = agent.generate(
        image_path=uploaded_image,
        prompt=prompt,
        output_dir=GENERATED_DIR,
        filename=unique_name,
    )

    return JSONResponse(
        {
            "status": "success",
            "filename": unique_name,
            "image_url": f"/images/{unique_name}",
        }
    )


@app.get("/images/{filename}")
async def get_generated_image(filename: str):
    """
    Return a generated image.
    """

    image_path = GENERATED_DIR / filename

    if not image_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Image not found.",
        )

    return FileResponse(image_path)


@app.post("/approve")
async def approve(request: ApproveRequest):
    """
    Approve a generated image.
    Instagram publishing will be connected after
    adding public image hosting.
    """

    image_path = GENERATED_DIR / request.filename

    if not image_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Image not found.",
        )

    # TODO:
    # Upload image to Cloudinary (or another public host)
    # public_url = upload_to_cloudinary(image_path)
    # instagram.post_image(public_url)

    return JSONResponse(
        {
            "status": "approved",
            "filename": request.filename,
            "message": "Image approved. Ready for Instagram publishing.",
        }
    )