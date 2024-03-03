import re

# IGNORECASE - is flag! - and ignore upper/lower letters.
string = "The quick brown fox jumps over the lazy dog. Python is fun. Programming is fun!"
match = re.search(r'\bp\w*', string, re.IGNORECASE)

if match:
    print(f"The first word in the string with 'p' is: {match.group()}")
else:
    print("No words starts with 'p' we found")