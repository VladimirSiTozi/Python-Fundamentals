import re


def matching_valid_locations(string):
    travel_places = []
    points = 0
    pattern = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'
    match = re.finditer(pattern, string)

    for current_place in match:
        travel_places.append(current_place.group(2))
        points += len(current_place.group(2))

    print(f"Destinations: {', '.join(travel_places)}\nTravel Points: {points}")


string = input()
matches = matching_valid_locations(string)

# "=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=
