from fastapi import APIRouter, Depends, Request, Response
from router import user
from schemas import UserBase
from database.database import get_db
from sqlalchemy.orm import Session
from database import db_user
from typing import List

router = APIRouter(
    prefix='/user',
    tags= ['USER']
)


@router.post('/', response_model= UserBase)
def create_user(request: UserBase, db: Session = Depends (get_db)):
    return db_user.create_user(db, request)


@router.get('/', response_model= List[UserBase])
def get_all_users(db:Session = Depends(get_db)):
    return db_user.get_all_users(db)