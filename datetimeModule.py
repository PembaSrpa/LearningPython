import datetime
import pytz

# Create a specific date
d = datetime.date(2025, 7, 18)
print(f"Specific date: {d}")

# Get today's date
tday = datetime.date.today()
print(f"Today's date: {tday}")

# Print year, month, and day from today's date
print(f"Year: {tday.year}, Month: {tday.month}, Day: {tday.day}")

# Print weekday (Monday=0)
print(f"Weekday (Monday=0): {tday.weekday()}")

# Print ISO weekday (Monday=1)
print(f"ISO Weekday (Monday=1): {tday.isoweekday()}")

# Create a timedelta of 7 days
tdelta = datetime.timedelta(days=7)

# Date 7 days from today
print(f"Date 7 days from today: {tday + tdelta}")

# Date 7 days before today
print(f"Date 7 days before today: {tday - tdelta}")

# Calculate days until birthday
bday = datetime.date(2025, 12, 22)
diff = bday - tday
print(f"Days until birthday (2025-12-22): {diff}")

# Create a time object
t = datetime.time(12, 30, 45)
print(f"Time object: {t}")

# Create a datetime object
dt = datetime.datetime(2025, 7, 18, 12, 30, 45)
print(f"Datetime object: {dt}")
print(f"Date part of datetime: {dt.date()}")
print(f"Time part of datetime: {dt.time()}")
print(f"Year of datetime: {dt.year}")

# Add timedelta to datetime
print(f"Datetime 7 days from given datetime: {dt + tdelta}")
tdelta2 = datetime.timedelta(hours=12)
print(f"Datetime 12 hours from given datetime: {dt + tdelta2}")

# Get current local datetime
dt1 = datetime.datetime.today()
dt2 = datetime.datetime.now()
dt3 = datetime.datetime.now(datetime.timezone.utc)
print(f"Current local datetime (today): {dt1}")
print(f"Current local datetime (now): {dt2}")
print(f"Current UTC datetime (timezone-aware): {dt3}")

# Create timezone-aware datetime in UTC
dat = datetime.datetime(2025, 7, 18, 12, 30, 45, tzinfo=pytz.utc)
print(f"Timezone-aware datetime (UTC): {dat}")
dat_now = datetime.datetime.now(pytz.utc)
print(f"Current UTC datetime (pytz): {dat_now}")
dat_utcnow = datetime.datetime.now(datetime.timezone.utc)
print(f"Current UTC datetime (datetime.timezone.utc): {dat_utcnow}")

# Convert UTC datetime to Nepal Time
dat_npl = dat_now.astimezone(pytz.timezone('Asia/Kathmandu'))
print(f"Current datetime in Nepal Time: {dat_npl}")

print(dat_npl.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
print(dat_npl.strftime("%B %d, %Y"))
dt_str = 'July 18, 2025'
dt4 = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(f"Parsed datetime from string: {dt4}")
# Format datetime to string
formatted_dt = dt4.strftime('%Y-%m-%d %H:%M:%S')
print(f"Formatted datetime: {formatted_dt}")
