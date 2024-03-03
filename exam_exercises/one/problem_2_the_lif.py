people_waiting = int(input())
state_of_the_lif = [int(num) for num in input().split()]
loaded_list = []

for wagons in state_of_the_lif:
    for man in range(people_waiting):
        if wagons == 4:
            loaded_list.append(wagons)
            break
        wagons += 1
        people_waiting -= 1
if 0 < wagons < 4:
    loaded_list.append(wagons)


if loaded_list[-1] < 4:
    loaded_list = [str(plp) for plp in loaded_list]
    print(f"The lift has empty spots! \n{' '.join(loaded_list)}")

if people_waiting > 0:
    loaded_list = [str(plp) for plp in loaded_list]
    print(f"There isn't enough space! {people_waiting} people in a queue!\n{' '.join(loaded_list)}")

