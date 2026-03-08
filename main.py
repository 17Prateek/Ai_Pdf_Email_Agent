from fastapi import FastAPI, UploadFile, File
import shutil
import os

from agents import run_workflow

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "AI PDF Agent Running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = run_workflow(file_path)

    return {"result": result}