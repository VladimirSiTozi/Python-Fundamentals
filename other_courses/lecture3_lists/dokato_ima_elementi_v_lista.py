zoo = ['DOG', 'CAT', 'MICE', 'BIRD']

index = 0
while zoo: # dokato ima neshte v lista
    print(zoo[index]) #принтираме елемента (cat)
    current_element = zoo[index] #запазваме променливата като елемент (cat)
    zoo.remove(current_element) #изваждаме елемнта (cat)

zoo1 = ['DOG', 'CAT', 'MICE', 'BIRD']
for i in range(len(zoo1)): # duljinata na lista
    print(zoo1[index])
    current_element = zoo1[index]
    zoo1.remove(current_element)