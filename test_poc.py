import requests

print_steps = False

user = "a"
user_hash = ord("a")

# print("Testing POC")
# r = requests.get("http://127.0.0.1:8000/pull/" + user, params={"hash": user_hash}).json()
# if print_steps:
#     print(r)

# r = requests.post("http://127.0.0.1:8000/push/" + user, json={"data": "test"}, params={"hash": user_hash})
# if print_steps:
#     print("post", r.json())

# res = requests.get("http://127.0.0.1:8000/pull/" + user, params={"hash": user_hash}).json()
# if print_steps:
#     print(res)
# if res["data"] == "test":
#     print("-Passed project test")
# else:
#     print("Didn't store test in user", user)
#     quit(1)

# user_hash = sum([ord(a) for a in "proj:"]) + user_hash
# r = requests.get("http://127.0.0.1:8000/pull/proj", params={"hash": user_hash, "entry": user}).json()
# if print_steps:
#     print(r)

# r = requests.post("http://127.0.0.1:8000/push/proj", json={"data": "test"}, params={"hash": user_hash, "entry": user})
# if print_steps:
#     print(r.json())

# res = requests.get("http://127.0.0.1:8000/pull/proj", params={"hash": user_hash, "entry": user}).json()
# if print_steps:
#     print(res)
# if res["data"] == "test":
#     print("-Passed entry test")

print("Real example")
user_hash = 2 * ord("C") + ord(":") + ord(user)
# r = requests.post("http://127.0.0.1:8000/push/CC", params={"hash": user_hash, "entry": user}, json={"data":"{\"passedHealthCheck\":false,\"_meta\":{\"dataVersion\":1,\"name\":\"Pickaxe\"},\"resources\":{\"Stick\":{\"isBase\":false,\"isDisabled\":false,\"durability\":-1,\"value\":1,\"tags\":[],\"name\":\"Stick\",\"baseQuantity\":1},\"Iron Ingot\":{\"isBase\":false,\"isDisabled\":false,\"durability\":-1,\"value\":1,\"tags\":[],\"name\":\"Iron Ingot\",\"baseQuantity\":1},\"Iron Ore\":{\"isBase\":true,\"isDisabled\":false,\"durability\":-1,\"value\":1,\"tags\":[],\"name\":\"Iron Ore\",\"baseQuantity\":1},\"Iron Pickaxe\":{\"isBase\":false,\"isDisabled\":false,\"durability\":-1,\"value\":1,\"tags\":[],\"name\":\"Iron Pickaxe\",\"baseQuantity\":1},\"Iron Nugget\":{\"isBase\":false,\"isDisabled\":false,\"durability\":-1,\"value\":1,\"tags\":[],\"name\":\"Iron Nugget\",\"baseQuantity\":1},\"Iron Block\":{\"isBase\":true,\"isDisabled\":true,\"durability\":-1,\"value\":1,\"tags\":[],\"name\":\"Iron Block\",\"baseQuantity\":1},\"Plank\":{\"isBase\":false,\"isDisabled\":false,\"durability\":-1,\"value\":1,\"tags\":[],\"name\":\"Plank\",\"baseQuantity\":1},\"Oak Log\":{\"isBase\":true,\"isDisabled\":false,\"durability\":-1,\"value\":1,\"tags\":[],\"name\":\"Oak Log\",\"baseQuantity\":1},\"Birch Log\":{\"isBase\":true,\"isDisabled\":false,\"durability\":-1,\"value\":1,\"tags\":[],\"name\":\"Birch Log\",\"baseQuantity\":1},\"Plank Dust\":{\"isBase\":false,\"isDisabled\":false,\"durability\":-1,\"value\":1,\"tags\":[],\"name\":\"Plank Dust\",\"baseQuantity\":1},\"Bucket\":{\"isBase\":false,\"isDisabled\":false,\"durability\":-1,\"value\":1,\"tags\":[],\"name\":\"Bucket\",\"baseQuantity\":1}},\"processes\":{\"Crafting Table\":{\"isBase\":false,\"isDisabled\":false,\"durability\":-1,\"value\":1,\"tags\":[],\"name\":\"Crafting Table\"},\"Furnace\":{\"isBase\":false,\"isDisabled\":false,\"durability\":-1,\"value\":1,\"tags\":[],\"name\":\"Furnace\"}},\"recipes\":[{\"processUsed\":\"Furnace\",\"inputResources\":[{\"resourceName\":\"Iron Ore\",\"amount\":1}],\"outputResources\":[{\"resourceName\":\"Iron Ingot\",\"amount\":1}],\"outputBonusChances\":[],\"timeSpent\":0,\"id\":0,\"isDisabled\":false,\"isBase\":false},{\"processUsed\":\"Crafting Table\",\"inputResources\":[{\"resourceName\":\"Iron Nugget\",\"amount\":9}],\"outputResources\":[{\"resourceName\":\"Iron Ingot\",\"amount\":1}],\"outputBonusChances\":[],\"timeSpent\":0,\"id\":1,\"isDisabled\":false,\"isBase\":false},{\"processUsed\":\"Crafting Table\",\"inputResources\":[{\"resourceName\":\"Iron Block\",\"amount\":1}],\"outputResources\":[{\"resourceName\":\"Iron Ingot\",\"amount\":9}],\"outputBonusChances\":[],\"timeSpent\":0,\"id\":2,\"isDisabled\":false,\"isBase\":false},{\"processUsed\":\"Crafting Table\",\"inputResources\":[{\"resourceName\":\"Stick\",\"amount\":3},{\"resourceName\":\"Iron Ingot\",\"amount\":3}],\"outputResources\":[{\"resourceName\":\"Iron Pickaxe\",\"amount\":1}],\"outputBonusChances\":[],\"timeSpent\":0,\"id\":3,\"isDisabled\":false,\"isBase\":false},{\"processUsed\":\"Crafting Table\",\"inputResources\":[{\"resourceName\":\"Iron Ingot\",\"amount\":1}],\"outputResources\":[{\"resourceName\":\"Iron Nugget\",\"amount\":9}],\"outputBonusChances\":[],\"timeSpent\":0,\"id\":4,\"isDisabled\":false,\"isBase\":false},{\"processUsed\":\"Crafting Table\",\"inputResources\":[{\"resourceName\":\"Plank\",\"amount\":1}],\"outputResources\":[{\"resourceName\":\"Stick\",\"amount\":2}],\"outputBonusChances\":[],\"timeSpent\":0,\"id\":5,\"isDisabled\":false,\"isBase\":false},{\"processUsed\":\"Crafting Table\",\"inputResources\":[{\"resourceName\":\"Oak Log\",\"amount\":1}],\"outputResources\":[{\"resourceName\":\"Plank\",\"amount\":2},{\"resourceName\":\"Plank Dust\",\"amount\":1}],\"outputBonusChances\":[],\"timeSpent\":0,\"id\":6,\"isDisabled\":false,\"isBase\":false},{\"processUsed\":\"Crafting Table\",\"inputResources\":[{\"resourceName\":\"Birch Log\",\"amount\":1}],\"outputResources\":[{\"resourceName\":\"Plank\",\"amount\":1}],\"outputBonusChances\":[],\"timeSpent\":0,\"id\":7,\"isDisabled\":false,\"isBase\":false},{\"processUsed\":\"Crafting Table\",\"inputResources\":[{\"resourceName\":\"Iron Ingot\",\"amount\":3}],\"outputResources\":[{\"resourceName\":\"Bucket\",\"amount\":1}],\"outputBonusChances\":[],\"timeSpent\":0,\"id\":8,\"isDisabled\":false,\"isBase\":false},{\"processUsed\":\"Crafting Table\",\"inputResources\":[{\"resourceName\":\"Oak Log\",\"amount\":2},{\"resourceName\":\"Iron Nugget\",\"amount\":3}],\"outputResources\":[{\"resourceName\":\"Iron Pickaxe\",\"amount\":1}],\"outputBonusChances\":[],\"timeSpent\":0,\"id\":9,\"isDisabled\":false,\"isBase\":false}]}"})
r = requests.post("http://127.0.0.1:8000/push/CC", params={"hash": user_hash, "entry": user}, json={"data": "poc"})
res = requests.get("http://127.0.0.1:8000/pull/CC", params={"hash": user_hash, "entry": user})
print(res.content)
