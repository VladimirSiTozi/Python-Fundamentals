num_list = [int(input()) for _ in range(2)]
print(f"Before:\na = {num_list[0]}\nb = {num_list[1]}")

num_list[0], num_list[1] = num_list[1], num_list[0]
print(f"After:\na = {num_list[0]}\nb = {num_list[1]}")