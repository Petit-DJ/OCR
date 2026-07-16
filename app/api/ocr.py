from fastapi import APIRouter, File, UploadFile
from PIL import Image
import pytesseract
from files import get_file
from files.get_file() import path


pytesseract.pytesseract.tesseract_cmd = 'C:/Users/YOUR_PATH_HERE'

image = get_file()
image = Image.open(path)

extracted_text = pytesseract.image_to_string(image)

print (extracted_text)
