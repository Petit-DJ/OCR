from fastapi import APIRouter, File, UploadFile
import shutil
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/DJSuryansh-BroadwayI/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

router = APIRouter (
    prefix='/file',
    tags=['file']
)

@router.post('/files')
def get_file (file: UploadFile = File(...)):
    path = f"files/{file.filename}"
    with  open(path, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)
    image = Image.open(path)
    ext_txt = pytesseract.image_to_string(image)

    return{
        'filename': path,
        'type': file.content_type,
        'text': ext_txt
    }