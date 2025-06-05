from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import sys
import json

# Redis has been postponed for now
# from redis import Redis


class Data(BaseModel):
    data: str


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

# Use dictionary as main data structure
USE_TEST = "redis" not in sys.argv
test_storage = dict()

# If using dict, should we store it somewhere for persistence?
storage_loc = os.environ.get("persist_loc", None)

invalid_resp = {"message": "Invalid request."}


def store_data(project_path: str, data: str):
    """
    Store data into chosen location.
    """
    global test_storage

    if USE_TEST:
        test_storage[project_path] = data
        # Save the updated dict.
        if storage_loc:
            with open(storage_loc, "w") as f:
                json.dump(test_storage, f)

    else:
        # r = Redis(host='localhost', port=6379)
        # r.set(project_path, data)
        pass


def get_data(project_path: str):
    """
    Try to retrieve the data that is in this location.
    """
    global test_storage

    if USE_TEST:
        # Load dict if at already exists with preexisting data.
        if storage_loc and os.path.exists(storage_loc):
            with open(storage_loc, "r") as f:
                test_storage = json.load(f)
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
        except KeyError:  # Don't do anything if it doesn't already exist
            pass
    else:  # Redis one
        pass


def name_patch(project: str, entry: str = None):
    """
    Merges the project and entry name in a Redis friendly way. It's slightly smarter than basic concatenation.
    """
    if entry:
        return project + ":" + entry
    else:
        return project

def calc_hash(name: str) -> int:
    return sum([ord(a) for a in name])


@app.get("/")
def root():
    """
    Test page.
    """
    return {"message": "Hello World"}


@app.get("/pull/{project}")
def get(project: str, entry: str = None, hash: int = None):
    """
    Get value at path.
    """
    path = name_patch(project, entry)
    if hash == calc_hash(path):
        return get_data(path)
    else:
        return invalid_resp


@app.post("/push/{project}")
def update(project: str, data: Data, entry: str = None, hash: int = None):
    """
    Set value at path.
    """
    path = name_patch(project, entry)
    if hash == calc_hash(path):
        store_data(path, data.data)
        return {"message": "Data saved"}
    else:
        return invalid_resp


@app.post("/reset/{project}")
def reset(project: str, entry: str = None, hash: int = None):
    """
    Remove any values at path.
    """
    path = name_patch(project, entry)
    if hash == calc_hash(path):
        reset_path(path)
        return {"message": "Cleared"}
    else:
        return invalid_resp

