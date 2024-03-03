import re

pattern = r'(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})'
dates = input()

matches = re.findall(pattern, dates)

for match in matches:
    day = match[0]
    separator = [1]
    month = match[2]
    year = match[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")

