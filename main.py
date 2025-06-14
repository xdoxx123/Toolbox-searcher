import requests
import time
import json
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

def GetUserInfo(userid: int):
    url = f"https://apis.roblox.com/toolbox-service/v1/marketplace/10?limit=1000&pageNumber=0&creatorType=1&creatorTargetId={userid}&includeOnlyVerifiedCreators=false"
    response = requests.get(url)
      
    return response.json()

def GetItemInfo(item: int):
    url = f"https://economy.roblox.com/v2/assets/{item}/details"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to get item {item}: {response.status_code}")
        return {}
    return response.json()

user_id = int(input("User id : "))

userinfo = GetUserInfo(user_id)

name = []
for i in userinfo.get("data", []):
    time.sleep(config["Timeout"])
    item_info = GetItemInfo(i["id"])
    
    name.append({"id": str(i["id"]), "name": item_info.get("name")})
    
        

print(name)

LogData = input("Log to a file? Y/N ")
if LogData.lower() != "y":
    exit()
else:
    
    with open(file=config["Logfilename"],mode="w") as f:
        json.dump(name,f)