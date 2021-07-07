import requests
from datetime import datetime
from pprint import pprint
import time
import json

now = int(datetime.timestamp(datetime.now()))
start = now - 2 * 86400

PARAMS = {
        'fromdate' : start,
        'todate' : now,
        'tagged' : 'python',
        'site' : 'stackoverflow',
        'pagesize' : 100,
        'sort' : 'creation'
    }

complete_data=[]
for i in range(30):
    response = requests.get("https://api.stackexchange.com/2.3/questions?page=" + str(i + 1), params=PARAMS)
    newData = json.loads(response.text)
    for item in newData['items']:
        complete_data.append(item['title'])
    print("Processed page " + str(i + 1) + ", returned " + str(response))
    time.sleep(5)
pprint(complete_data)

