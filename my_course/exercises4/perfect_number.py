def perfect_num(num):
    perfect = []
    for x in range(1, num +1):
        if num % x == 0:
            perfect.append(x)
    return perfect

number = int(input())
nums_list = perfect_num(number)
sum_of_nums = sum(nums_list)

if sum_of_nums % number == 0:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")