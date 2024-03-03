numbers = [int(num) for num in input().split()]
average_of_nums = sum(numbers) / len((numbers))
numbers.sort()
reversed_list = list(reversed(numbers))

final_list = []

for tops in range(5):
    top_five = max(reversed_list)
    if top_five > average_of_nums:
        final_list.append(top_five)
        reversed_list.remove(top_five)

if len(final_list) == 0:
    print("No")
else:
    final_list = [str(x) for x in final_list]
    print(" ".join(final_list))