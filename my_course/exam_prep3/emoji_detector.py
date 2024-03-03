import re


def cool_points_function(initial_text):
    pattern = r'[0-9]'
    match = re.findall(pattern, initial_text)
    return match


def emoji_detector_function(initial_text):
    pattern = r'((:{2}|\*{2})([A-Z]{1}[a-z]{2,})\1)'
    match = re.findall(pattern, initial_text)
    emojis = []
    for emoji in match:
        emojis.append(emoji[1])
    return emojis


def emoji_coolness_point_detector(emojis_list, total_cool_points):
    for emoji in emojis_list:
        emoji_points = 0
        for char in emoji:
            emoji_points += ord(char)

        if emoji_points >= total_cool_points:
            print()


initial_text = input()
coolness_points = cool_points_function(initial_text)
total_cool_points = 1

for x in coolness_points:
    total_cool_points *= int(x)

emojis_list = emoji_detector_function(initial_text)
emoji_coolness_point_detector(emojis_list, total_cool_points)



