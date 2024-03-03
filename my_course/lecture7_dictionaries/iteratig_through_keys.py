student = {
    'name': 'Ivan',
    'age': 25,
    'major': 'Computer Science',
    'gpa': 3.8
}

for k in student.keys():
    print(k, end=" ")

print(f"\n")

for v in student.values():
    print(f"{v}", end=' ')

print(f"\n")
# multiply the values

for ke in student.keys():
    student[ke] *= 2
print(f"{student}")
