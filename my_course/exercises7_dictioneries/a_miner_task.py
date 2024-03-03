my_resources = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())

    if resource not in my_resources.keys():
        my_resources[resource] = 0
    my_resources[resource] += quantity

for key, value in my_resources.items():
    print(f"{key} -> {value}")