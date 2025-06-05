import requests

user = "a"
user_hash = ord("a")

print("Testing POC")
print(requests.get("http://127.0.0.1:8000/pull/" + user, params={"hash": user_hash}).json())

r = requests.post("http://127.0.0.1:8000/push/" + user, json={"data": "test"}, params={"hash": user_hash})
print(r.json())

res = requests.get("http://127.0.0.1:8000/pull/" + user, params={"hash": user_hash}).json()
print(res)
if res == {"data": "test"}:
    print("Passed project test")

user_hash = sum([ord(a) for a in "proj:"]) + user_hash
print(requests.get("http://127.0.0.1:8000/pull/proj", params={"hash": user_hash, "entry": user}).json())

r = requests.post("http://127.0.0.1:8000/push/proj", json={"data": "test"}, params={"hash": user_hash, "entry": user})
print(r.json())

res = requests.get("http://127.0.0.1:8000/pull/proj", params={"hash": user_hash, "entry": user}).json()
print(res)
if res == {"data": "test"}:
    print("Passed entry test")
