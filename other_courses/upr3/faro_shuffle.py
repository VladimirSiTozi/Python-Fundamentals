import random

cards = input().split(" ")
shuffles = int(input())

for _ in range(shuffles):
        for current_shuffle in cards:
                if current_shuffle == [0]:
                        continue
                elif current_shuffle == [-1]:
                        continue
                else:random.shuffle(cards)

print(cards)
# cards = input().split()
# shuffles = int(input())
#
# for _ in range(shuffles):
#     first_half = cards[:len(cards)//2]
#     second_half = cards[len(cards)//2:]
#     cards = [card for pair in zip(first_half, second_half) for card in pair]
#
# print(' '.join(cards))