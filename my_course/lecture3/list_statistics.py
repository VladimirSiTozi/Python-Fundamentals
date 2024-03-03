n = int(input())
number_positive = []
number_negative = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        number_positive.append(number)
    else:
        number_negative.append(number)

print(number_positive)
print(number_negative)
print(f"Count of positives: {len(number_positive)}")
print(f"Sum of negatives: {sum(number_negative)}")