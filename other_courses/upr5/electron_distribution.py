number_of_electrons_input = int(input())
shell = 0
shells_lst = []
electrons_counter = 0

while number_of_electrons_input > 0:
    shell += 1
    electrons = 2 * shell ** 2
    electrons_counter += electrons
    number_of_electrons_input -= electrons
    if number_of_electrons_input < 0:
        electrons += number_of_electrons_input
        shells_lst.append(electrons)
        break
    shells_lst.append(electrons)

print(shells_lst)