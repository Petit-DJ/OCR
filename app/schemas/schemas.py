from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    username: str
    email: str
    # class config():
    #     orm_mode = True

class OcrBase (BaseModel):
    ocr_id: int
    file_name: str
    ocr_text: str
