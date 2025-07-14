#DRY = Dont repeat yourself
def hello_func():
    pass # doesnt do anything but used to not throw errors

hello_func()
print(hello_func())

def hi_func():
    print('Hi')

hi_func()
hi_func()

def idk_func():
    return 'idk'

print(idk_func())

def add(a, b):
    return a + b

print(add(2,3))

def greet(greeting, name = 'You'):
    return '{} {} Function.'.format(greeting, name)

print(greet('Hello'))
print(greet('Hello' ,'Duck'))

def student_info(*args, **kwargs): #we use these because we dont know how many values we will use or smtg like that
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age='21')
# args = tuple with all our positional arguments
# kwargs = dictionary with all our kweyword values

courses = ['Math', 'Art']
info = {'name':'Jane', 'age':'23'}

# student_info(courses, info) We have to unpack it
student_info(*courses, **info)


#Example
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#first value placeholder for indexing purposes

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
