from fastapi import FastAPI
from pydantic import BaseModel

from redis import Redis


class Data(BaseModel):
    data: str


app = FastAPI()
USETEST = False
test_storage = dict()


def store_data(user_id: str, data: str):
    if USETEST:
        test_storage[user_id] = data
    else:
        r = Redis(host='localhost', port=6379)
        r.set(user_id, data.replace(":", ""))


def get_data(user_id: str):
    if USETEST:
        try:
            return {"data": test_storage[user_id]}
        except KeyError:
            return {"error": "No data for this user"}
    else:
        r = Redis(host='localhost', port=6379)
        return {"data": r.get(user_id)}


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/pull/{user_id}")
def get(user_id: str):
    return get_data(user_id)


@app.post("/push/{user_id}")
def post(user_id: str, data: Data):
    store_data(user_id, data.data)
    return {"message": "Data saved"}


