import calendar
import datetime
import math
import os
import random
import sys  # where python looks for modules

import antigravity
import mymodule as mm
from mymodule import *  # to import everything, not good
from mymodule import find_index  # to import function itself

# sys.path.append('/home/nirashanichang/Desktop/Python Projects/Learnings/modules/')

courses = ['Art', 'Nepali', 'English', 'Maths', 'CompSci']

index = mm.find_index(courses, 'Maths')
print(index)
index1 = find_index(courses, 'Art')
print(index1)

print(sys.path)

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

print(os.getcwd()) #current working directory
print(os.__file__)
