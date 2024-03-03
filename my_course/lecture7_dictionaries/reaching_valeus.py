student = {
    'name': 'Ivan',
    'age': 25,
    'major': 'Computer Science',
    'gpa': 3.8
}

print(student['name'])
# or
print(student.get('major'))

# get None
print(student.get('address'))

# KeyError
# print(student['address'])
