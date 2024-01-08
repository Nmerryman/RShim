from fastapi import FastAPI
from pydantic import BaseModel

from redis import Redis


class Data(BaseModel):
    data: str


app = FastAPI()
USETEST = False
test_storage = dict()


def store_data(project_path: str, data: str):
    if USETEST:
        test_storage[project_path] = data
    else:
        r = Redis(host='localhost', port=6379)
        r.set(project_path, data)


def get_data(project_path: str):
    if USETEST:
        try:
            return {"data": test_storage[project_path]}
        except KeyError:
            return {"error": "No data for this user"}
    else:
        r = Redis(host='localhost', port=6379)
        return {"data": r.get(project_path)}


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/pull/{project}")
def get(project: str, entry: str = None):
    if entry:
        entry = ":" + entry
    else:
        entry = ""
    return get_data(project + entry)


@app.post("/push/{project}")
def post(project: str, data: Data, entry: str = None):
    if entry:
        entry = ":" + entry
    else:
        entry = ""
    store_data(project + entry, data.data)
    return {"message": "Data saved"}


