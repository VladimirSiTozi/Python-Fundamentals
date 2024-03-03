symbols = [char for char in input() if char != " "]
letters = {}

for char in symbols:
    if char not in letters.keys():
        letters[char] = 1
    else:
        letters[char] += 1

for k in letters:
    print(f"{k} -> {letters[k]}")