number_of_messages = int(input())

for _ in range(number_of_messages):
    digit = int(input())

    if digit == 88:
        print("Hello")
    elif digit == 86:
        print("How are you?")
    elif digit < 86 or digit == 87:
        print("GREAT!")
    elif digit > 88:
        print("Bye.")