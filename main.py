from fastapi import FastAPI
from router import user

ramesh = FastAPI()


ramesh.include_router(user.router)

@ramesh.get('/hello')
def hello():
    return {"sandesh": "MGMA"}
