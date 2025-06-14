import requests
import time
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
speed = True
userinfo = GetUserInfo(user_id)

name = []
for i in userinfo.get("data", []):
    item_info = GetItemInfo(i["id"])
    
    name.append({"id": str(i["id"]), "name": item_info.get("name", "Unknown")})
    if speed == False:
        time.sleep(0.5)
        

print(name)
