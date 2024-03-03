following_lines = int(input())
all_even = True

for _ in range(following_lines):
    num = int(input())
    if num % 2 != 0:
        print(f"{num} is odd!")
        all_even = False
        break

if all_even:
    print("All numbers are even.")