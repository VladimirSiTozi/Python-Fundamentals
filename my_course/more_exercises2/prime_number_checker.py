given_number = int(input())
flag = False

if given_number == 1:
    flag = False
elif given_number > 1:
    for i in range(2, given_number):
        if given_number % i == 0:
            flag = True
            break
if flag:
    print("False")
else:
    print("True")