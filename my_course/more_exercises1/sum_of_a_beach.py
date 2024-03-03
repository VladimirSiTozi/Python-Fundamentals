given_string = input().lower()
special_words = ["sand", "water", "fish", "sun"]
counter = 0

for word in special_words:
    how_many_times = given_string.count(word)
    counter += how_many_times

print(counter)