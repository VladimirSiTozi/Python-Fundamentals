print("Enter both racers times:", end="")
numbers = input().split()
left_racer = []
right_racer = []
numbers_as_int = []

for numb in numbers:
    value_of_num = int(numb)
    numbers_as_int.append(value_of_num)

idx_right = [-1, -2, -3, -4, -5]
right_racer = [numbers_as_int[i] for i in idx_right]
idx_left = [0, 1, 2, 3, 4]
left_racer = [numbers_as_int[i] for i in idx_left]

total_right = 0
total_left = 0
for number in right_racer:
    if number != 0:
        total_right += number
    elif number == 0:
        total_right *= 0.8

for number1 in left_racer:
    if number1 != 0:
        total_left += number1
    elif number1 == 0:
        total_left *= 0.8

print(f"Time of the left racer: {total_left:.2f} seconds")
print(f"Time of the right racer: {total_right:.2f} seconds")

if total_right < total_left:
    print(f"The winner is right_racer with total time: {total_right:.2f} seconds.")
else:
    print(f"The winner is left_racer with total time: {total_left:.2f} seconds.")