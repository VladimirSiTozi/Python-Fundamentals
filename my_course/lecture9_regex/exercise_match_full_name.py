import re


def match_name(name):
    pattern = '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'
    matches = re.findall(pattern, name)
    return matches


name = input()

print(' '.join(match_name(name)))

# Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett