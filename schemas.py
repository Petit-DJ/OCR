from pydantic import BaseModel


class UserBase(BaseModel):
    user_id: int
    username: str
    email: str
    class config():
        orm_mode = True

class Img (BaseModel):
    img_id: int
    extracted_text: str

