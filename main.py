from fastapi import FastAPI, APIRouter, Request, Response
from app.api import user
from app.api import files, ocr
from app.database import db_models
from app.database.database import engine


ramesh = FastAPI()

ramesh.include_router(ocr.router)
ramesh.include_router(user.router)
ramesh.include_router(files.router)
@ramesh.get('/hello')
def hello():
    return {"sandesh": "MGMA"}

# Create tables
db_models.Base.metadata.create_all(engine)