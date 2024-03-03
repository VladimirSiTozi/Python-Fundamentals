number_of_snowballs = int(input())
highest_score = 0
top_wight = 0
top_time = 0
top_quality = 0

for snowballs in range(number_of_snowballs):
    weight_of_the_snowball = int(input())
    time_needed = int(input())
    quality = int(input())
    current_score = (weight_of_the_snowball / time_needed) ** quality
    if current_score > highest_score:
        highest_score = current_score
        top_wight = weight_of_the_snowball
        top_time = time_needed
        top_quality = quality
print(f"{top_wight} : {top_time} = {int(highest_score)} ({top_quality})")
