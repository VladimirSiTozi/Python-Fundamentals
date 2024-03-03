import re

# group of two ORs
text = 'The ball is red and big'
pattern = '(red|blue) and (big|small)'

result = re.findall(pattern, text)
print(result)