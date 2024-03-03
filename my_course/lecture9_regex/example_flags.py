import re

# Ignore upper/lower letters
text = 'Hello world.'
print(re.findall('hello', text))
print(re.findall('hello', text, re.IGNORECASE))