from fastapi import APIRouter, File, UploadFile
from PIL import Image
import pytesseract
from files import get_file
from files.get_file() import path


pytesseract.pytesseract.tesseract_cmd = 'C:/Users/DJSuryansh-BroadwayI/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

image = get_file()
image = Image.open(path)

extracted_text = pytesseract.image_to_string(image)

print (extracted_text)
