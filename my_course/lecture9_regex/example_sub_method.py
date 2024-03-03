import re

# replace sth with sth else
string = 'There are 3 dogs and 4 cats.'
result = re.sub('\d', 'number', string)
print(result)

# same + shows how many times sth has been replaced.
string1 = 'There are 3 dogs and 4 cats.'
result1 = re.subn('\d', 'number', string)
print(result1)