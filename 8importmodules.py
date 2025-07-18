# filepath: /home/nirashanichang/Desktop/Python Projects/Learnings/8importmodules.py
# Demonstrates importing modules and using their functions

import calendar
import datetime
import math
import os
import random
import sys  # System-specific parameters and functions

import antigravity  # Fun Easter egg module
import mymodule as mm
from mymodule import *           # Import all (not recommended)
from mymodule import find_index  # Import specific function

# sys.path.append('/path/to/modules/')  # Add custom module path

courses = ['Art', 'Nepali', 'English', 'Maths', 'CompSci']

index = mm.find_index(courses, 'Maths')
print(index)
index1 = find_index(courses, 'Art')
print(index1)

print(sys.path)  # List of module search paths

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))  # Check for leap year

print(os.getcwd())  # Current working directory
print(os.__file__)  # Location of os module
