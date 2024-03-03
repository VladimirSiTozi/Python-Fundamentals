from math import ceil

number_of_the_students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
counter_of_lectures = 0

for students in range(number_of_the_students):
    attendances = int(input())
    total_bonus = (attendances / lectures) * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        counter_of_lectures = attendances

print(f"Max Bonus: {ceil(max_bonus)}")
print(f"The student has attended {counter_of_lectures} lectures.")