import re

text = 'Python is an interpreted language.'
pattern = '[arn]'

result = re.findall(pattern, text)
print(result)
print(result.count('n'))

# ------------------------------------
# range
text = 'Python is an interpreted language.'
pattern = '[a-n]'

result = re.findall(pattern, text)
print(result)

# --------------------------------
# Everything expect those letters
text = 'Python is an interpreted language.'
pattern = '[^arn]'

result = re.findall(pattern, text)
print(result)


