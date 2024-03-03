even = []
odd = []
positive = []
negative = []

while True:
    numbers = input()

    if numbers == 'even':
        print(even)
        break
    elif numbers == 'odd':
        print(odd)
        break
    elif numbers == 'negative':
        print(negative)
        break
    elif numbers == 'positive':
        print(positive)
        break

    if int(numbers) % 2 == 0:
        even.append(numbers)
    elif int(numbers) % 2 != 0:
        odd.append(numbers)

    if int(numbers) < 0:
        negative.append(numbers)
    else:
        positive.append((numbers))