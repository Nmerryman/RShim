from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
import sys
import json

# Redis has been postponed for now
# from redis import Redis


class Data(BaseModel):  # Network message
    data: str

# class StorageEntry(BaseModel):
#     data: str
#     password: Optional[str] = None
# type StorageEntry = dict[str, str]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"]
)

# Use dictionary as main data structure
USE_TEST = "redis" not in sys.argv
test_storage: dict[str, dict[str, str]] = dict()

# If using dict, should we store it somewhere for persistence?
storage_loc = os.environ.get("persist_loc", None)


def store_data(project_path: str, data: dict[str, str]):
    """
    Store data into chosen location.
    """
    global test_storage

    if USE_TEST:

        test_storage[project_path] = data
        # Save the updated dict.
        if storage_loc:
            with open(storage_loc + "/" + project_path, "w") as f:
                json.dump(data, f)

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
        # if storage_loc and os.path.exists(storage_loc):
        #     with open(storage_loc + "/" + project_path, "r") as f:
        #         test_storage = json.load(f)
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
            return {"error": data["error"]}
        print(data)
        return {"data": data["data"]["data"], "hasPassword": data["data"]["password"] is not None}
    else:
        return {"error": "Invalid Hash."}


@app.post("/push/{project}")
def update(project: str, data: Data, entry: str = None, hash: int = None, password: str = None):
    """
    Set value at path.
    """
    path = name_patch(project, entry)
    if hash == calc_hash(path):     # Permit write?
        existing = get_data(path)
        if "error" in existing:
            if existing["error"] == "No data for this user":
                store_data(path, {"data": data.data, "password": password})
                return {"message": "Data saved"}
            else:
                return {"error": existing["error"]}
        existing_data: dict[str, str] = existing["data"]
        if existing_data["password"] is None or existing_data["password"] == password:
            store_data(path, {"data": data.data, "password": password})
            return {"message": "Data saved"}
        else:
            return {"error", "Incorrect password"}
    else:
        return {"error": "Invalid Hash."}


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
        return {"error": "Invalid Hash."}

