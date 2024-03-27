from fastapi import APIRouter, UploadFile, Request, File
import shutil

from app.pages.router import templates
from app.tasks.tasks import process_pic

router = APIRouter(prefix="/images", tags=["Upload Image"])


@router.post("/upload-files")
async def add_hotel_image(request: Request, file: UploadFile = File(...)):
    if not file:
        raise
    img_path = f"app/static/images/{file.filename}"
    with open(img_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_pic.delay(img_path)
    return templates.TemplateResponse("success.html", context={"request": request})
