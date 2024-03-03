animal = []

for _ in range(3):
    word = input()
    animal.append(word)

animal[0], animal[2] = animal[2], animal[0]
print(animal)
