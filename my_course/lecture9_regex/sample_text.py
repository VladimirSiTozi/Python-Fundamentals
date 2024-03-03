import re

# hi
text = 'hi, hiiiii, hiiiiiiiiiiiii, hii'
pattern = 'hi'
    
result = re.findall(pattern, text)
print(result)

# hi*

text = 'hi, hiiiii, hiiiiiiiiiiiii, hii'
pattern = 'hi*'

result = re.findall(pattern, text)
print(result)