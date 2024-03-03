student = {
    'name': 'Ivan',
    'age': 25,
    'major': 'Computer Science',
    'gpa': 3.8
}

print(student.keys())
print(student.values())
print(student.items())

for k, v in student.items():
    print(k, v)