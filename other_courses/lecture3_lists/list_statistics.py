number_of_lines = int(input())
positive_lst = []
negative_lst = []

for i in range(number_of_lines):
    current_number = int(input())

    if current_number >= 0:
        positive_lst.append(current_number)
    else:
        negative_lst.append(current_number)

print(f"Positive number {positive_lst}")
print(f"Negative number {negative_lst}")
print(f"Count of positives: {len(positive_lst)}")
print(f"Sum of negatives: {sum(negative_lst)}")
