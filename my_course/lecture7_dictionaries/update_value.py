student = {
    'name': 'Ivan',
    'age': 25,
    'major': 'Computer Science',
    'gpa': 3.8
}

print(student.get('age'))

student['age'] = 29
print(student.get('age'))

# to add (if not in the dict)
student['address'] = "Vidin"
print(student)