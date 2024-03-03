import re

s = 'Readability counts.'
pattern = r'[aeoui]'

matches = re.finditer(pattern, s)
for match in matches:
    print(match)
