from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
import sys
import json

# Redis has been postponed for now
# from redis import Redis


class Data(BaseModel):
    data: str

class storageEntry(BaseModel):
    data: str
    password: Optional[str] = None


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

# Use dictionary as main data structure
USE_TEST = "redis" not in sys.argv
test_storage: dict[str, storageEntry] = dict()

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
        # r = Redis(host='localhost', port=6379)
        # return {"data": r.get(project_path)}
        return {"error": "Redis missing"}


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
        data = get_data(path)
        if "error" in data:
            return data
        return {"data": data["data"].data}
    else:
        return invalid_resp


@app.post("/push/{project}")
def update(project: str, data: Data, entry: str = None, hash: int = None, password: str = None):
    """
    Set value at path.
    """
    path = name_patch(project, entry)
    if hash == calc_hash(path):     # Permit write?
        existing = get_data(path)
        if "error" in existing:
            return existing
        data: storageEntry = existing["data"]
        if data.password is None or data.password == password:
            store_data(path, data.data)
            return {"message": "Data saved"}
        else:
            return {"error", "Incorrect password"}
    else:
        return invalid_resp


@app.post("/reset/{project}")
def reset(project: str, entry: str = None, hash: int = None, secret: int = 0):
    """
    Remove any values at path.
    """
    path = name_patch(project, entry)
    if hash == calc_hash(path) and secret == 2:
        reset_path(path)
        return {"message": "Cleared"}
    else:
        return invalid_resp

