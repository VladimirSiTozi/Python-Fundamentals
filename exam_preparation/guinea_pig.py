food, hay, cover = float(input()) * 1000, float(input()) * 1000, float(input()) * 1000
pigs_weight = float(input()) * 1000

for days in range(1, 31):
    if food and hay and cover <= 0:
        break

    food -= 300
    if days % 2 == 0:
        hay -= food * 0.05
    if days % 3 == 0:
        cover -= pigs_weight * (1/3)

if food >= 0 and hay >= 0 and cover >= 0:
    print(f"Everything is fine! Puppy is happy! Food: {(food / 1000):.2f}, Hay: {(hay / 1000):.2f}, Cover: "
          f"{(cover / 1000):.2f}.")
else:
    print("Merry must go to the pet store!")
