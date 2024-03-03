text = input()
new_text = [char for char in text if char not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(new_text))
