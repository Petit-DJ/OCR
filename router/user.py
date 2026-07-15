from fastapi import APIRouter, Depends
from router import user
from schemas import UserBase
from database.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/user',
    tags= ['USER']
)


@router.post('/', response_model =UserBase)
def create_user(request = UserBase, db: Session = Depends (get_db)):
    return db_user.create_user(db, request)


@router.get('/user')
def get_user():
    pass