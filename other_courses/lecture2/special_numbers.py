# number = int(input())
# for i in range(1, number+1, +1):
#     print(i[:2])


n = int(input())
for i in range(1, n+1):
    digits_sum = sum(int(d) for d in str(i))
    is_special = (digits_sum == 5) or (digits_sum == 7) or (digits_sum == 11)
    print(f"{i} -> {is_special}")