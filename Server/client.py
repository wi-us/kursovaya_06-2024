import requests
import json

SERVER = "http://192.168.1.12:8001"
PATHS = {   "user":"/user/",
            "table":"/table/",
            "booking":"/booking/",}

def serializeJson(obj : dict) -> str:
    return json.dumps(obj)

def deserializeJson(string : str) -> str:
    return json.loads(string)

"""
на поступает словать с определнными названиями переменных
"""
strJson = serializeJson({"guestCountMax":2, "vipStatus":False})

header = {
    "Content-Type": "application/json; charset=utf-8",
}
print(requests.post(url=f"{SERVER}/{PATHS["user"]}", headers=header, data=strJson))
"""
data должна быть сериализованной строкой
"""