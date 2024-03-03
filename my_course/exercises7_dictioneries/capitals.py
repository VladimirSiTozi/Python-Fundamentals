countries = input().split(", ")
capitals = input().split(", ")

information = {countries[index]: capitals[index] for index in range(len(countries))}

for key, value in information.items():
    print(f'{key} -> {value}')