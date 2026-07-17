from sqlalchemy.orm.session import Session
from app.database.db_models import DbOcr
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

def get_ocr_det( user_id: int, db: Session ):
    return db.query(DbOcr).all()

def get_user_details(unique_id: int, db: Session):
    return db.query(DbOcr).filter(DbOcr.unique_id == unique_id).all()
