import requests
from time import sleep
import json
import os

with open('./seeds_temp.json') as f:
    data = json.load(f)

url = "https://mighty-lake-45709.herokuapp.com/temperatures/"
TOKEN = os.environ['TOKEN']
headers = {"Authorization": TOKEN}

for i in data:
    r = requests.post(url, headers=headers, data={
        "temperature": i["temperature"],
            "date": i["date"],
            "time": i["time"]
    } )
    print(r.status_code)
    print(r.content)
    sleep(0.5)
