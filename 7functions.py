# Demonstrates function definitions and usage

# DRY = Don't Repeat Yourself

def hello_func():
    pass  # Placeholder function

hello_func()
print(hello_func())  # Returns None

def hi_func():
    print('Hi')

hi_func()
hi_func()

def idk_func():
    return 'idk'

print(idk_func())

def add(a, b):
    return a + b

print(add(2, 3))

def greet(greeting, name='You'):
    return '{} {} Function.'.format(greeting, name)

print(greet('Hello'))
print(greet('Hello', 'Duck'))

# *args and **kwargs for variable arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age='21')

courses = ['Math', 'Art']
info = {'name': 'Jane', 'age': '23'}

# Unpacking lists and dicts into function arguments
student_info(*courses, **info)

# Example: Leap year and days in month
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Returns True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year"""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2017))
print(days_in_month(2017, 2))
