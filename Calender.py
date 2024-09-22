import calendar
import datetime
current = datetime.datetime.now()
year = current.year
month = current.month
print(calendar.month(year, month))