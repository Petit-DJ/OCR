from fastapi import APIRouter, Depends, Request, Response
from app.schemas.schemas import OcrResponse             
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.database import db_ocr
from typing import List

router = APIRouter(
    prefix= "/ocr",
    tags= ['OCR']
)


#GET 1 OCR OF 1 USER
@router.get('/1_user', response_model= List[OcrResponse])
def get_ocr_det(id: int, db: Session = Depends(get_db)):
    return db_ocr.get_ocr_det(id, db)

# #GET ALL UPLODS OF 1 USER
# @router.get('/user_details', response_model= List[OcrResponse])
# def get_user_details(unique_id: int, db: Session = Depends(get_db)):
#     return db_ocr.get_user_details(unique_id, db)

@router.get("/user_details")
def get_user_details(
    unique_id: int,
    db: Session = Depends(get_db)
):
    records = db_ocr.get_user_details( unique_id, db)

    print(records[0].user.username)

    return records