def length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def characters(username):
    for ch in username:
        if ch.isalnum() or ch == "-" or ch == "_":
            return True
        return False


def symbols(username):
    if " " in username:
        return False
    return True


def user_name_is_valid(username):
    if length(username) and characters(username) and symbols(username):
        return True
    return False


user_names = input().split(", ")

for username in user_names:
    if user_name_is_valid(username):
        print(username)
