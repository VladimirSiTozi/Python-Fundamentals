numbers = [int(num) for num in input().split(" ")]
total_sum = sum(numbers)
average_number = total_sum / len(numbers)
over_average = []
top_five = []

for nums in numbers:
    if nums > average_number:
        over_average.append(nums)

for tops in range(5):
    top_num = max(over_average)
    top_five.append(top_num)
    over_average.remove(top_num)
print(top_five)