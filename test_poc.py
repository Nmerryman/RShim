import requests

user = "a"

print("Testing POC")
print(requests.get("http://127.0.0.1:8000/pull/" + user).json())

r = requests.post("http://127.0.0.1:8000/push/" + user, json={"data": "test"})
print(r.json())

print(requests.get("http://127.0.0.1:8000/pull/" + user).json())
