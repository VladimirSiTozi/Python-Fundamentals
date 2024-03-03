while True:
    string = input()
    output = ""

    if string == "End":
        break
    elif string == "SoftUni":
        continue
    else:
        for i in string:
            output += i * 2
    print(output)