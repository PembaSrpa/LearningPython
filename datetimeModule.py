# Demonstrates date and time operations using the datetime module

import datetime  # Import the datetime module for date and time operations

# Create a specific date object (year, month, day)
d = datetime.date(2025, 7, 18)
print(d)  # Output: 2025-07-18

# Get today's date
tday = datetime.date.today()
print(tday)  # Output: current date

# Print year, month, and day of today's date
print(tday.year, tday.month, tday.day)

# Print the weekday (Monday=0, Sunday=6)
print(tday.weekday())  # Output: integer representing the weekday

# Print the ISO weekday (Monday=1, Sunday=7)
print(tday.isoweekday())  # Output: integer representing the ISO weekday

# Create a timedelta object representing 7 days
tdelta = datetime.timedelta(days=7)

# Add 7 days to today's date
print(tday + tdelta)  # Output: date 7 days from today

# Subtract 7 days from today's date
print(tday - tdelta)  # Output: date 7 days before today

