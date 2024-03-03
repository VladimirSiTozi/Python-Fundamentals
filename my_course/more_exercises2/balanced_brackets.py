n_lines = int(input())
flag = False
bracket_list = []

for _ in range(n_lines):
    string = input()
    if string in ["(", ")"]:
        bracket_list.append(string)

for index, bracket in enumerate(bracket_list):
    if index % 2 == 0 and bracket == "(":
        flag = True
    else:
        flag = False
        break
    if index % 2 == 1 and bracket == ")":
        flag = True
    else:
        flag = False
        break

if flag:
    print("BALANCED")
else:
    print("UNBALANCED")