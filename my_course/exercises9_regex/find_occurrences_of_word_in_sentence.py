import re


def matching(sentence, word):
    pattern = fr'\b{word}\b'
    match = re.findall(pattern, sentence, re.IGNORECASE)
    return match


sentence = input()
word = input()

print(len(matching(sentence, word)))

# input
# The waterfall was so high, that the child couldn't see its peak.
# the
#
# How do you plan on achieving that? How? How can you even think of that?
# how
#
# There was one. Therefore I bought it. I wouldn't buy it otherwise.
# there
