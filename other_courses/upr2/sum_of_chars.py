number = int(input())
sum_of = 0

for i in range(number):
    letter = ord(input())
    sum_of += letter

print(f"The sum equals: {sum_of}")