from stackapi import StackAPI, StackAPIError
from datetime import datetime

now = int(datetime.timestamp(datetime.now()))
start = now - 2 * 86400

SITE = StackAPI("stackoverflow")
SITE.max_pages=30
SITE.page_size=100
questions = SITE.fetch('questions', sort='creation', fromdate=start, todate=now, tagged='python')
for question in questions['items']:
        print('Question: ', question['title'])
        date_a = question['creation_date']
        value = datetime.fromtimestamp(date_a)
        date_b = value.strftime('%Y-%m-%d %H:%M:%S')
        print('Date: ', date_b)