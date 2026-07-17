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


# Returns all users in a json format. It's got magic, conv .py code into sqllite
def get_all_users(db: Session):
    return db.query(DbUser).all()

#Returns 1 user
def get_one_user(id: int, db: Session):
    return db.query(DbUser).filter(DbUser.id == id).first()