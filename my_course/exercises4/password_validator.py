import re


def password_validator(my_pass):
    if not 6 <= len(my_pass) <= 10:
        print("Password must be between 6 and 10 characters")

    pattern_is_digit_and_letters = '[A-Za-z0-9]'
    match_only_digit_and_letters = re.search(pattern_is_digit_and_letters, my_pass)
    if not match_only_digit_and_letters:
        print("Password must consist only of letters and digits")

    pattern_is_two_digit = '[0-9]{2,}'
    match_two_digits = re.search(pattern_is_two_digit, my_pass)
    if not match_two_digits:
        print("Password must have at least 2 digits")

    if 6 < len(my_pass) < 10 and match_only_digit_and_letters and match_two_digits:
        print('Password is valid')


password = input()
password_validator(password)

