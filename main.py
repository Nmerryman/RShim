from fastapi import FastAPI
from pydantic import BaseModel

from redis import Redis


class Data(BaseModel):
    data: str


app = FastAPI()
USETEST = True
test_storage = dict()


def store_data(user_id: str, data: str):
    if USETEST:
        test_storage[user_id] = data



@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/pull/{user_id}")
def get(user_id: str):
    try:
        return {"data": test_storage[user_id]}
    except KeyError:
        return {"error": "No data for this user"}


@app.post("/push/{user_id}")
def post(user_id: str, data: Data):
    store_data(user_id, data.data)
    return {"message": "Data saved"}


