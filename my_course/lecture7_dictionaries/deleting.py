student = {
    'name': 'Ivan',
    'age': 25,
    'major': 'Computer Science',
    'gpa': 3.8
}
# deleting the dict
# del student

# del key
del student['age']
print(student)

# pop key
value = student.pop('name')
print(student)