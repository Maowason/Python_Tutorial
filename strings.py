message = 'Madhhav\'s'  # Escape

message = "Madhhav's"  # Using double quotes instead

message = """Madhhav is a
Very Good Boy"""  # Multi line printing

print(message)

print(len(message))  # To check the length of message

print(message[3])  # Print a particular Character of string

print(message[0:7])  # Slicing - Print a range of characters of string
print(message[:7])  # Same as above
print(message[:])  # Full list

print(message.lower())  # lower case
print(message.upper())  # Upper case
print(message.count('h'))  # counts the number of 'h'
# Returns the index where word starts, -1 if not there
print(message.find('Good'))


message = 'Hello World'
new_message = message.replace('World', 'Universe')
print(new_message)


greeting = 'Hello'
name = 'Madhhav'
message = greeting + ', ' + name + '. Welcome!'
# But better than using + is to use formated strings
message = '{}, {}. Welcome!'.format(greeting, name)

# But even better than that is to use fstrings
message = f'{greeting}, {name}. Welcome!'
message = f'{greeting.upper()}, {name}. Welcome!'
print(message)

# Now if we face trouble remembering these functions then use print(dir(name)) or print(help(str)) or print(help(str.lower))

# ----------------------------------------------------------------------
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9  These are the indexes
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1  These are the negative indexes
print(my_list[1:-2])


print(my_list[0:5])  # Goes up till 4 since end is non inclusive

# my_list[start:stop:step]

print(my_list[-2:1:-2])
print(my_list[::-1])  # Full list in reverse


# ----------------------------------------------------------------------
person = {'name': 'Jenn', 'age': 23}
sentence = 'My name is {} and I am {} years old'.format(
    person['name'], person['age'])
# OR
sentence = 'My name is {0} and I am {1} years old'.format(
    person['name'], person['age'])
# OR
sentence = 'My name is {0[name]} and I am {1[age]} years old'.format(
    person, person)
# OR
sentence = 'My name is {0[name]} and I am {0[age]} years old'.format(
    person)
# OR
l = ['Jenn', 23]
sentence = 'My name is {0[0]} and I am {0[1]} years old'.format(l)

print(sentence)

# The case is slightly different for Classes and instances


class Person():
    """docstring for Person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', 23)
sentence = 'My name is {0.name} and I am {0.age} years old'.format(p1)
print(sentence)


# Most Readable way of formatting
person = {'name': 'Jenn', 'age': 23}
sentence = 'My name is {name} and I am {age} years old'.format(**person)
print(sentence)


# {:} the colon is used to specify that we wanna do some formatting
#  For loop printing formatting
for i in range(1, 11):
    # This is zero padding - adding zeroes before the value
    sentence = 'The value is {:03}'.format(i)
    print(sentence)

# This is for printing upto some decimal places
pi = 3.14159265
sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)

# Adding a comma seperator through formatting
sentence = '1MB is equal to {:,} bytes'.format(1000**2)
# Now for both comma and decimal places we can do this:
sentence = '1MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)


# To format and print out dates we can do this:
import datetime
my_date = datetime.datetime(2020, 7, 27, 12, 30, 45)
print(my_date)

# Now lets say we wanted in format of August 27, 2020
# Check the documentation to find the directive such as %B, %Y etc... then
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# Now lets say we wanna do:
# July 27, 2020 fell on Monday and was the 209 day of the year
sentence = '{0:%B %d, %Y} fell on {0:%A} and was the {0:%j} day of the year'.format(
    my_date)
print(sentence)
