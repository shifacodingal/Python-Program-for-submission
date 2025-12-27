from datetime import datetime, timedelta

now = datetime.now()

first_day_year = datetime(now.year, 1, 1)
first_day_month = datetime(now.year, now.month, 1)
first_day_week = now - timedelta(days=now.weekday())

print("First day of the year:", first_day_year.strftime("%Y-%m-%d"))
print("First day of the month:", first_day_month.strftime("%Y-%m-%d"))
print("First day of the week:", first_day_week.strftime("%Y-%m-%d"))
