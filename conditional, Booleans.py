if True:
    print('Conditional was True')
if False:
    print('Conditional was True')  # Wont Print

language = 'Python'
if language == 'Python':
    print('Conditional was True')

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Idendity:  is

# is  <== Will check if values have the same id or
# basically if they are in the same object/memory


language = 'Python'
if language == 'Python':
    print('Language is Python')
else:
    print('No Match')

# elif
language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match')

# Python does not have switch case cause if, elif and else are clean enough to do this

# Boolean:
# and
# or
# not

user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:  # All true is true
    print('Admin Page')
else:
    print('Bad Creds')

user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in:  # Any one true is true
    print('Admin Page')
else:
    print('Bad Creds')

user = 'Admin'
logged_in = False
if not logged_in:  # not False became True
    print('Please log in')
else:
    print('Welcome')


# is
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # returns True

print(id(a))
print(id(b))
print(a is b)  # returns False since different objects in memory

# But what if we make them equal
b = a
print(id(a))
print(id(b))
print(a == b)  # True
print(a is b)  # Now it'll return True cause id's are same

# is  <== id(a) == id(b)


# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence, eg: '', (), []
# Any empty mapping, for eg: {}

# So we can use something like this to check if a sequence or mapping is empty.
