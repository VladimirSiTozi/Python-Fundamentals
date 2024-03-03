import string
import re

students = []
course_to_search = ''

while True:
    student_info = input()

    if ':' not in student_info:
        course_to_search = student_info
        break

    name, ID, course = student_info.split(':')
    students.append({'name': name, 'ID': ID, 'course': course})

# removing punctuation from word
chars = re.escape(string.punctuation)
course_to_search = re.sub('['+chars+']', ' ', course_to_search)

for student in students:
    if student['course'] == course_to_search:
        print(f"{student['name']} - {student['ID']}")