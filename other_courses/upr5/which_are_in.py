first_sequence = input().split(", ")
second_sequence = input().split(", ")
substring = []

for first_word in first_sequence:
    for second_word in second_sequence:
        if first_word in second_word:
            substring.append(first_word)
            break
print(substring)

# test input
# arp, live, strong
# lively, alive, harp, sharp, armstrong
#
# tarp, mice, bull
# lively, alive, harp, sharp, armstrong

