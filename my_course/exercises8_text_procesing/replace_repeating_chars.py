import re

text = input()
pattern = r'(\w)\1+'

match = re.sub(pattern, r'\1', text)

print(match)

# test input
# aaaaabbbbbcdddeeeedssaa

# qqqwerqwecccwd