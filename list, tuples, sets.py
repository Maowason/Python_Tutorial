# List and Tuples allow us to work with sequential data
# Sets are unordered collection of values with no duplicates.

# Lists----
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))  # length of list
print(courses[2])  # Using indexes to access list values
# We can also use of negative indexes
print(courses[-1])  # Easier way to access last item
# To get the range of values
print(courses[0:2])
# This is same as:
print(courses[:2])  # This is all slicing

# To add new item to list:
courses.append('Art')
print(courses)

# Now what if we want to append at a certain location:
# We will now use insert() instead of append()
courses.insert(0, 'Biology')
print(courses)

# Another way to add values is to use extend() but lets see what happens with insert
courses_2 = ['Chemistry', 'Education']
# courses.insert(0, courses_2)
print(courses)
# So lets see what happens with extend()
courses.extend(courses_2)
print(courses)

# Now that we have seen how to append/insert/extend lets see how to remove
courses.remove('Math')
print(courses)

courses.pop()
print(courses)  # This will just remove the top/last
# Pop will not only remove the last element but it also returns it
popped = courses.pop()
print(courses)
print(popped)

# Reverse
courses.reverse()
print(courses)

# Sorting - ascending
courses.sort()
print(courses)

# Sorting - descending
courses.sort(reverse=True)  # This will print in descending
print(courses)

# But what if we do not wish to alter the actual list, this is  where sorted() is used
num = [4, 3, 5, 1, 2]
sorted_num = sorted(num)
print(sorted_num)

# min(), max() and sum()
print(min(num))
print(max(num))
print(sum(num))


# To search for index of a particular element of list:
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses.index('CompSci'))

# To check if element in list or not:
# We will use the in operator
print('Art' in courses)  # which will return false

for item in courses:
    print(item)
# Now if we also want the index we will use the enumerate() function
# enumerate() returns both index and the list item
for index, item in enumerate(courses):
    print(index, item)
# We can also give a start value to the index in enumerate()
for index, item in enumerate(courses, start=1):
    print(index, item)


# Now we can seperate list items and make a string using join()
course_str = ', '.join(courses)
print(course_str)

# Now if we wanna convert a symbol seperated string to list we will use split()
new_list = course_str.split(', ')
print(new_list)


# Tuples--------------------------------------------------------------

# One major difference btween tuples and lists is that we cannot modify tuples
# Lists are mutable tuples are immutable

# Mutable
list_1 = ['History', 'Math', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)
# So after running this we see that index 0 value changes to Art now lets try this with tuples

# Immutable
list_1 = ('History', 'Math', 'CompSci')
list_2 = list_1
print(list_1)
print(list_2)

# list_1[0] = 'Art'  <== This will return an error cause tuples are immutable
# print(list_1)
# print(list_2)


# Sets--------------------------------------------------------------

# Sets are values that are unordered and have no duplicates

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)
# This will print in random orders because unlike list or tuples sets
# dont care about order cause some of the main uses of the set is to check
# if a value is part of the set and also to remove duplicate values

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses)  # Removes Duplicate Math

# Membership test - To check if element is part of set
# List and tuples can also do this bt sets are optimized for it

print('Math' in cs_courses)  # Returns True

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# Above are all the functionalities of Sets

# -----------------------
# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This is WRONG! It's a dictionary
empty_set = set()
