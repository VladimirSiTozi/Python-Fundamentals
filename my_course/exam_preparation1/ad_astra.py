import re


def calculating(food):
    pattern = r'(\||\#)(?P<name>[A-Za-z\s]+)(\1)(?P<date>[0-9]{2}\/[0-9]{2}\/[0-9-]{2})(\1)(?P<cal>[0-9]{1,5})(\1)'
    total_cal = 0
    food_items = []
    matches = re.finditer(pattern, food)

    for match in matches:
        item = match.groupdict()
        item['cal'] = int(item['cal'])
        total_cal += item['cal']
        food_items.append(item)

    available_food = total_cal // 2000
    print(f"You have food to last you for: {available_food} days!")

    for item in food_items:
        print(f"Item: {item['name']}, Best before: {item['date']}, Nutrition: {item['cal']}")


food_info = input()
result = calculating(food_info)

# test inputs

# $$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19.03.20#450|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe|Milk|05/09/20|2000|

# Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|

# Hello|#Invalid food#19/03/20#450|$5*(@
