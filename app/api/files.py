from fastapi import APIRouter, File, UploadFile, Request, Response, Depends
import shutil
from PIL import Image
import pytesseract
from app.schemas.schemas import OcrBase, OcrResponse
from app.database import db_ocr
from sqlalchemy.orm import Session
from app.database.database import get_db
from typing import List

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/DJSuryansh-BroadwayI/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

router = APIRouter (
    prefix='/file',
    tags=['file']
)

@router.post('/files/{id}' )
def get_file (id: int,    file: UploadFile = File(...),  db: Session = Depends (get_db)):
    path = f"files/{file.filename}"
    with  open(path, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)
    image = Image.open(path)
    ocr_txt = pytesseract.image_to_string(image)

    return db_ocr.get_ocr(
    db,
    path,
    ocr_txt,
    id
)

    # { 'filename': path,
    #     'type': file.content_type,
    #     'text': ocr_txt
    # }

# , response_model= List [OcrResponse] request: OcrBase,