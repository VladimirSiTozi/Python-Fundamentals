money = input().split(", ")
money_listed_as_a_digit = []
# take number, but as s str ["1", "2", "3", "4", "5"]

for element in money:
    money_listed_as_a_digit.append(int(element))
# convert them into int [1, 2, 3, 4, 5]

number_of_beggars = int(input()) # how many are beggars
final_sum = []
starting_index = 0

while starting_index < number_of_beggars:
    sum_for_current_beggar = 0

    for current_index in range(starting_index, len(money_listed_as_a_digit), number_of_beggars):
        sum_for_current_beggar += money_listed_as_a_digit[current_index]

    final_sum.append(sum_for_current_beggar)
    starting_index += 1

print(final_sum)