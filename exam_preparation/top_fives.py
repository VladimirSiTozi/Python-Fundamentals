numbers = [int(num) for num in input().split(" ")]
total_sum = sum(numbers)
average_number = total_sum / len(numbers)
over_average = []
top_five = []

for nums in numbers:
    if nums > average_number:
        over_average.append(nums)

over_average.sort()
over_average.reverse()

for tops in over_average:
    if len(top_five) == 5:
        break
    if tops > average_number:
        top_five.append(tops)

top_five = [str(num) for num in top_five]
print(" ".join(top_five))
if len(top_five) == 0:
    print("No")