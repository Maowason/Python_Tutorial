
def hello_func():
    pass  # We can just leave it blank by using pass


print(hello_func)
# Without the paranthesis it just tells that it is a function at some location

print(hello_func())  # Will just return None


def hello_func():
    print('hello Function!')


hello_func()
hello_func()
hello_func()
hello_func()

# Now if we make one change to the fucntion's print that will change it in all 4 statements
# This is called:
# Keeping your code DRY!
# Dont Repeat Yourself


def hello_func():
    return 'hello Function!'


print(hello_func())

print(hello_func().upper())


def hello_func(greeting, name='You'):  # Adding an argument with a default value to the argument
    return '{} {}'.format(greeting, name)


print(hello_func('Hi', 'Madhhav'))
print(hello_func('Hi', name='Madhhav'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age=22)

# Allows us to accept an arbitrary number of positional or keywords arguments
# args and kwargs are just conventions
# args - positional arguments, will return tuples
# kwargs - key word arguments, it is a dictionary with the key word values

# Sometimes we will encouter a functin call  with argumesnt using * and **
# It'll unpack sequence and dictionary and will pas them to the function individually


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)  # Wont work
student_info(*courses, **info)
# This will work


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    '''Return True for leap year, False for non-leap year'''  # DOCSTRING - Explains what fucntions do
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    '''Return number of days in that month in that year'''
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]
