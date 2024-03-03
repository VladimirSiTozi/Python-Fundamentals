import re

# starts with '^Python'
text = 'Python is fun'
pattern = '^Python'
result = re.findall(pattern, text)
print(result)


# 'fun\.$' ends with "fun."
text = 'Python is fun.'
pattern = 'fun\.$'
result = re.findall(pattern, text)
print(result)


# 'fun$' ends with "fun"
text = 'Python is fun'
pattern = 'fun$'
result = re.findall(pattern, text)
print(result)