students = {
    'Gosho': {'Math': 5, 'Chemistry': 6, 'English': 5, 'Biology': 4},
    'Ivan': {'Math': 2, 'Chemistry': 3, 'English': 3, 'Biology': 2},
    'Ivo': {'Math': 4, 'Chemistry': 4, 'English': 3, 'Biology': 4},
    'Maria': {'Math': 6, 'Chemistry': 6, 'English': 6, 'Biology': 6}
}

for student, record in students.items():
    print(student, record)
    print(student)
    for subject, score in record.items():
        print(subject, score)
    print()