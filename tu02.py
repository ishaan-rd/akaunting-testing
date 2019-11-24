from datetime import datetime
from datetime import timedelta

next_week = datetime.now() + timedelta(days=7)
print(next_week)