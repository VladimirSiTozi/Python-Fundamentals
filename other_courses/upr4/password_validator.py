def is_valid_length(passw):
    return 6 <= len(passw) <= 10


def is_pass_only_letters_and_digits(passw):
    return passw.isalnum()


def at_least_two_digits(passw):
    digit_counter = 0
    for x in passw:
        if 48 <= ord(x) <= 57:
            digit_counter += 1
    return digit_counter >= 2



password = input()

if is_valid_length(password) == False:
    print("Password must be between 6 and 10 characters")
if is_pass_only_letters_and_digits(password) == False:
    print("Password must consist only of letters and digits")
if at_least_two_digits(password) == False:
    print("Password must have at least 2 digits")

if is_valid_length(password) and is_pass_only_letters_and_digits(password) and at_least_two_digits(password) == True:
    print("Password is valid")