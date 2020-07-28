import my_module

courses = ['History', 'Math', 'Physics', 'Compsci']

index = my_module.find_index(courses, 'Math')
print(index)

# Now we can also make the modulename shorter

import my_module as mm

index = mm.find_index(courses, 'Math')  # Works fine
print(index)

# Now there is a way to import the function itself

from my_module import find_index  # This only gives us access to that function
index = find_index(courses, 'Math')  # Works fine
print(index)

# This only gives us access to that function
# Gives us access  to both test and function
from my_module import find_index, test_string
index = find_index(courses, 'Math')  # Works fine
print(index)
print(test_string)


# This will make the function name shorter
from my_module import find_index as fi  # It should be readable though
index = fi(courses, 'Math')  # Works fine
print(index)


# Not recommended since now we dont know where did find_index() come from
from my_module import *
index = find_index(courses, 'Math')  # Works fine
print(index)
print(test_string)


import sys
print(sys.path)  # Will show the order in which python checks for files

# First it'll check in the directory where we are running the script
# Then it'll check in the python path
# Then in std libraries dir
# Then in the site-packages

# But we can append new paths also----
# sys.path.append('/Users/.....')
# print(sys.path)

import random
courses = ['History', 'Math', 'Physics', 'Compsci']
random_course = random.choice(courses)
print(random_course)


import math
rads = math.radians(90)
print(math.sin(rads))


import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))


import os  # Will give us access to underlying OS
print(os.getcwd())  # Get current working dir
print(os.__file__)
