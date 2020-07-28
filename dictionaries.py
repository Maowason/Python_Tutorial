# Dictionaries allow us to work with Key:Value pairs

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

# Print only a certain key
print(student['name'])
print(student['courses'])

# So our keys and values can be multiple types
student_test = {1: 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student_test[1])  # Setting the key as an integer also works fine

# We will get a Keyerror when a key is not present in the dict
# print(student['phone'])  <== This will return an error
# So better to use get() method

print(student.get('phone'))
# No error, just prints None

# Even better is to specify a default value if the key doesnt exist
print(student.get('phone', 'Not Found!'))


# Adding another Key to the dictionary:
student['phone'] = '9103480230'
print(student.get('phone'))

# If a key already exists, then it'll update it's value
student['name'] = 'Maowason'
print(student)


# We can also update multiple values using update() function
student.update({'name': 'Mao', 'age': 30, 'phone': '9129372384'})
print(student)


# Delete a key and value using del
del student['age']
print(student)


student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# Delete using pop
age = student.pop('age')
print(student)
print(age)

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# To check number of keys use len()
print(len(student))

# To Print out all the keys:
print(student.keys())

# To Print out all the Values:
print(student.values())

# To print both keys and values, we will use this next
print(student.items())

# To loop through the dictionary:
for key, value in student.items():
    print(key, value)
