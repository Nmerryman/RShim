from fastapi import FastAPI
from pydantic import BaseModel

from redis import Redis
# Redis has been postponed for now


class Data(BaseModel):
    data: str


app = FastAPI()
USE_TEST = True
test_storage = dict()


def store_data(project_path: str, data: str):
    if USE_TEST:
        test_storage[project_path] = data
    else:
        r = Redis(host='localhost', port=6379)
        r.set(project_path, data)


def get_data(project_path: str):
    if USE_TEST:
        try:
            return {"data": test_storage[project_path]}
        except KeyError:
            return {"error": "No data for this user"}
    else:
        r = Redis(host='localhost', port=6379)
        return {"data": r.get(project_path)}


def reset_path(path: str):
    """
    Reset a specific value to be nothing
    """
    if USE_TEST:
        try:
            del test_storage[path]
        except KeyError:
            pass
    else:  # Redis one
        pass


def name_patch(project: str, entry: str = None):
    if entry:
        return project + ":" + entry
    else:
        return project


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/pull/{project}")
def get(project: str, entry: str = None):
    path = name_patch(project, entry)
    return get_data(path)


@app.post("/push/{project}")
def update(project: str, data: Data, entry: str = None):
    path = name_patch(project, entry)
    store_data(path, data.data)
    return {"message": "Data saved"}


@app.post("/reset/{project}")
def reset(project: str, entry: str = None):
    path = name_patch(project, entry)
    reset_path(path)
    return {"message": "Cleared"}

