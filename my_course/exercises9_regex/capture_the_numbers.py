import re

line = input()
while line:
    pattern = '\d+'
    matches = re.findall(pattern, line)
    if matches:
        print(' '.join(matches), end=' ')
    line = input()

# The300
# What is that?
# I think it's the 3rd movie
# Let's watch it at 22:45
