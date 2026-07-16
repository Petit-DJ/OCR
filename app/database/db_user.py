from sqlalchemy.orm.session import Session
from app.database.db_models import DbUser
from fastapi import Request
from app.schemas.schemas import UserBase

# Create 
def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,      
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
