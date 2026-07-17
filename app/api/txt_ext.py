# The file is only for text extraction, it shows basic implementation of tesseract
"""  
Image
↓
PIL
↓
pytesseract
↓
tesseract.exe   
↓
text
"""


from fastapi import APIRouter, File, UploadFile
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Users\DJSuryansh-BroadwayI\AppData\Local\Programs\Tesseract-OCR'



# 1. Open the image file using Pillow
image = Image.open('boh.jpg')

# 2. Convert the image text into a Python string
extracted_text = pytesseract.image_to_string(image)

# 3. Print the text result
print(extracted_text)
