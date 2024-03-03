import re


text = input()
pattern = ':[^\s]'

matches = re.findall(pattern, text)

for match in matches:
    print(match)