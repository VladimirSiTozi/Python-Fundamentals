import re


def matching(line):
    pattern = r'\b_([a-zA-Z0-9]+)\b'
    match = re.findall(pattern, line)
    return match


line = input()
result = matching(line)
print(','.join(result))

# input
# The _id and _age variables are both integers.
# Calculate the _area of the _perfectRectangle object.
# __invalidVariable _evenMoreInvalidVariable_ _validVariable
