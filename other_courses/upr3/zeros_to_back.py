numbers = input().split(", ")

zeros = []
non_zeros = []

for num in numbers:
    if num == "0":
        zeros.append(num)
    else:
        non_zeros.append(num)

result = non_zeros + zeros
print(result)