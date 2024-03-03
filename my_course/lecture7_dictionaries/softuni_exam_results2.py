users_points = {}
courses = {}

while True:
    current_result = input().split('-')

    if len(current_result) == 1:
        break

    elif len(current_result) == 2:
        name = current_result[0]
        del users_points[name]

    elif len(current_result) == 3:
        name, language, points = current_result[0], current_result[1], int(current_result[2])

        if language not in courses.keys():
            courses[language] = 0
        courses[language] += 1

        if name not in users_points.keys():
            users_points[name] = points
        else:
            if users_points[name] < points:
                users_points[name] = points

print('Results:')
for key_name, value_point in users_points.items():
    print(f"{key_name} | {value_point}")

print('Submissions:')
for key_submission, value_submission in courses.items():
    print(f"{key_submission} - {value_submission}")