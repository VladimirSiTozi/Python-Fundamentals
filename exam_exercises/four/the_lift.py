max_per_wagon = 4
people_waiting = int(input())
current_state_of_the_lift = [int(people) for people in input().split()]
number_of_wagons = 0

for index, wagon in enumerate(current_state_of_the_lift):
    if people_waiting == 0:
        break
    if people_waiting < max_per_wagon:
        current_state_of_the_lift[index] = people_waiting + current_state_of_the_lift[index]
        people_waiting -= wagon
        people_waiting -= people_waiting
        break
    if wagon == max_per_wagon:
        continue
    else:
        people_to_fill = max_per_wagon - wagon
        people_waiting -= people_to_fill
        wagon += people_to_fill
        current_state_of_the_lift[index] = wagon

if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")

if current_state_of_the_lift[-1] < 4:
    print("The lift has empty spots!")

current_state_of_the_lift = [str(x) for x in current_state_of_the_lift]
print(" ".join(current_state_of_the_lift))