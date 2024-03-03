# How to create a dictionaries

# 1) with cycles
keys = ['name', 'age', 'major']
values = ['Ivan', 25, 'Computer Science']

student0 = {}

for i in range(len(keys)):
    key = keys[i]
    value = values[i]
    student0[key] = value

print(f"Student0 - {student0}")

# 2) or with dict method
student1 = dict(name='Gosho', age=30, major='Chemistry')
print(f"Student1 - {student1}")

# 3) or inside of list, using tuples
student2 = dict([("name", 'Pesho'), ("age", 16), ("major", 'Sports')])
print(f"Student2 - {student2}")

# 4) or using zip method
keys1 = ['name', 'age', 'major']
values1 = ['Georgi', 21, 'Math']

student3 = dict(zip(keys1, values1))

print(f"Student3 - {student3}")
