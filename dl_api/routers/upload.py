from fastapi import APIRouter, File, UploadFile, Depends
from fastapi.responses import JSONResponse, FileResponse
import os
from ..dependencies import init_model

router = APIRouter(
    prefix="/upload",
    tags=["upload"],  # For Swagger header
)

# Get an image repsonse


@router.get("/", response_class=FileResponse)
async def get_image():
    fullpath = os.path.join(os.getcwd(), "uploads", "20210212_122649.jpg")

    return FileResponse(fullpath)

# Post method with UploadFile


@router.post("/", response_class=FileResponse)
async def upload_file(file: UploadFile = File(..., description="File to upload")):
    folderpath = os.path.join(os.getcwd(), "uploads")
    isExist = os.path.exists(folderpath)

    if not isExist:
        os.mkdir(folderpath)

    fullpath = os.path.join(os.getcwd(), "uploads", file.filename)

    await file.seek(0)
    with open(fullpath, "wb") as buffer:
        while True:
            content = await file.read(2 ** 20)
            if not content:
                break
            buffer.write(content)

    return FileResponse(fullpath)

# Detect image is dog or cat


@router.post("/detect", response_class=JSONResponse)
async def cat_dog_detect(file: UploadFile = File(..., description="File to upload"), local_model=Depends(init_model)):
    request_object_content = await file.read()  # Read file content

    result = local_model(file=request_object_content)  # Call model

    return {"message": result}
