zoo = ['DOG', 'CAT', 'MICE', 'BIRD']

zoo.pop(1) # remove by index
print(zoo)

zoo.remove("DOG") # remove by element
print(zoo)

new_zoo = ['DOG', 'CAT', 'MICE', 'BIRD', 'DOG', 'DOG']
a = new_zoo.count("DOG")
for i in range(a):
    new_zoo.remove("DOG")
print(new_zoo)

next_new_zoo = ['DOG', 'CAT', 'MICE', 'BIRD', 'DOG', 'DOG']
while next_new_zoo:
    a = next_new_zoo.count("DOG")
    next_new_zoo.remove("DOG")
print(next_new_zoo)