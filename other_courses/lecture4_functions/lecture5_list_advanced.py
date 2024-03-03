text = input()
forbidden_letters = ['a', 'o', 'u', 'e', 'i']
result = [char for char in text if char.lower() not in forbidden_letters]

print(result)
print(''.join(result))

# text = input()
# result = []
#
# for char in text:
#     # case insensitive (a, A, o, O ....)
#     if char.lower() not in ['a', 'o', 'u', 'e', 'i']:
#         result.append(char)
#
# print(result)
# print(''.join(result))

#List comprehansion

