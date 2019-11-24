from datetime import datetime
from datetime import timedelta

next_week = datetime.now().date() + timedelta(days=7)
nw = next_week.strftime('%Y-%m-%d')
print(nw)
print(type(nw))