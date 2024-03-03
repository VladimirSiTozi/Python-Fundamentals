my_list = []

for i in range(3):
    animal_part = input()
    my_list.append(animal_part)

my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)