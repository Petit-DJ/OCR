from sqlalchemy.orm.session import Session
from app.database.db_models import DbUser, DbOcr
from fastapi import Request
from app.schemas.schemas import UserBase, OcrBase

def get_ocr(db: Session, file_name: str, ocr_text: str, user_id: int):
    new_ocr = DbOcr(
        file_name=file_name,
        ocr_text=ocr_text,
        unique_id=user_id
    )

    db.add(new_ocr)
    db.commit()
    db.refresh(new_ocr)
    return new_ocr