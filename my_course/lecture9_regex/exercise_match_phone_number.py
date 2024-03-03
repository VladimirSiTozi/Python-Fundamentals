import re


def match_name(name):
    pattern = '\\+359-2-\d{3}-\d{4}\\b|\+359 2 \d{3} \d{4}\\b'
    matches = re.findall(pattern, phone_number)
    return matches

phone_number = input()

print(', '.join(match_name(phone_number)))

# +359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222