population = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())

for index, person in enumerate(population):
    richest = max(population)
    index_of_the_richest = population.index(richest)
    if richest <= minimum_wealth:
        break
    if person < minimum_wealth:
        to_give = minimum_wealth - person
        population[index_of_the_richest] -= to_give
        population[index] += to_give

if min(population) < minimum_wealth:
    print("No equal distribution possible")
else:
    print(population)