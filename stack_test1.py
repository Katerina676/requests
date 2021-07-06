import requests
from datetime import datetime
from pprint import pprint

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
resp = requests.get('https://api.stackexchange.com/2.3/questions', params = PARAMS)
for question in resp.json().get('items'):
        print('Question: ', question['title'])
        date_a = question['creation_date']
        value = datetime.fromtimestamp(date_a)
        date_b = value.strftime('%Y-%m-%d %H:%M:%S')
        print('Date: ', date_b)
