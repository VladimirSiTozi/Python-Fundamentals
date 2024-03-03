import re

text = 'The cost is 12.99 lv.'
pattern = '\d+\.\d+'

# findall - returns list
result = re.findall(pattern, text)
print(result)

# -----------------------------------
# \d
text2 = 'The year is 2023.'
pattern2 = '\d'

# findall - returns list
result2 = re.findall(pattern2, text2)
print(result2)

# \d+
text3 = 'The year is 2023.'
pattern3 = '\d+'

# findall - returns list
result3 = re.findall(pattern3, text3)
print(result3)