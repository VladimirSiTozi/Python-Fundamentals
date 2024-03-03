import re

# cat OR dog
text = 'cat, fish, bird'
pattern = 'cat|dog'

result = re.findall(pattern, text)
print(result)

# cat OR dog
text2 = 'cat, fish, bird, dog'
pattern2 = 'cat|dog'

result2 = re.findall(pattern2, text2)
print(result2)