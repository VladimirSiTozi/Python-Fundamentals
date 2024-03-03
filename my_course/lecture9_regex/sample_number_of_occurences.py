import re

# group of two ORs
text = '1234, 123, 12, 798, 123456, 1'
pattern = '\d{3}'

result = re.findall(pattern, text)
print(result)