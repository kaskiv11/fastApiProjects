from fastapi import FastAPI, UploadFile, File,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import shutil


app = FastAPI()

if not os.path.exists("static/temp"):
    os.makedirs("static/temp")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/upload.html", 'r') as file:
        html_content = file.read()
        return HTMLResponse(content=html_content)

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
ALLOWED_FILE_TYPES = ["image/png", "image/jpeg", "image/gif"]


@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):

    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed: {', '.join(ALLOWED_FILE_TYPES)}"
        )

    file_content = file.file.read()
    if len(file_content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"File is too large. Max size allowed is {MAX_FILE_SIZE//(1024*1024)} MB."
        )

    file_path = f"static/temp/{file.filename}"
    with open(file_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "file_path": file_path}


