from fastapi import FastAPI, APIRouter, Request, Response
from router import user, files
from database import db_models
from database.database import engine


ramesh = FastAPI()


ramesh.include_router(user.router)
ramesh.include_router(files.router)
@ramesh.get('/hello')
def hello():
    return {"sandesh": "MGMA"}

# Create tables
db_models.Base.metadata.create_all(engine)