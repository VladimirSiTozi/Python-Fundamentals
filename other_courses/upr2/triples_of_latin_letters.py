number = int(input())

for a in range(number):
    for b in range(number):
        for c in range(number):
            print(f"{chr(97 + a)}{chr(97 + b)}{chr(97 + c)}")