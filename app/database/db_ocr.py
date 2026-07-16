from sqlalchemy.orm.session import Session
from app.database.db_models import DbUser, DbOcr
from fastapi import Request
from app.schemas.schemas import UserBase, OcrBase


def get_ocr(db:Session, request: OcrBase):
    new_ocr = DbOcr (
        file_name = request.file_name,
        ocr_text = request.ocr_text
    )

    db.add(new_ocr)
    db.commit()
    db.refresh()
    return new_ocr