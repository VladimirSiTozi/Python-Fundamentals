import operator

lst = [1, 2, 3, 4, 5, 1]
lst2 = ["1", "2", "3", "4",  "5", "1"]

idx = [-1, -2, -3]

right = [lst[i] for i in idx]
print(lst)
print(right)
