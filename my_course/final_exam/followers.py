def base_function(jane_facebook):
    while True:
        command = input()
        if command.startswith('Log out'):
            log_out_function(jane_facebook)
            break
        elif command.startswith('New follower'):
            jane_facebook = new_follower_function(jane_facebook, command)

        elif command.startswith('Like'):
            jane_facebook = like_function(jane_facebook, command)

        elif command.startswith('Comment'):
            jane_facebook = comment_function(jane_facebook, command)

        elif command.startswith('Blocked'):
            jane_facebook = blocked_function(jane_facebook, command)


def new_follower_function(jane_facebook, current_command):
    action, follower = current_command.split(': ')
    if follower not in jane_facebook:
        jane_facebook[follower] = {'Likes': 0, 'Comments': 0}
    return jane_facebook


def like_function(jane_facebook, current_command):
    action, follower, count = current_command.split(': ')
    if follower not in jane_facebook:
        jane_facebook[follower] = {'Likes': int(count), 'Comments': 0}
    else:
        jane_facebook[follower]['Likes'] += int(count)
    return jane_facebook


def comment_function(jane_facebook, current_command):
    action, follower = current_command.split(': ')
    if follower not in jane_facebook:
        jane_facebook[follower] = {'Likes': 0, 'Comments': 1}
    else:
        jane_facebook[follower]['Comments'] += 1
    return jane_facebook


def blocked_function(jane_facebook, current_command):
    action, follower = current_command.split(': ')
    if follower not in jane_facebook:
        print(f"{follower} doesn't exist.")
    else:
        del jane_facebook[follower]
    return jane_facebook


def log_out_function(jane_facebook):
    print(f'{len(jane_facebook)} followers')
    for follower in jane_facebook:
        total_like_and_comments = jane_facebook[follower]['Likes'] + jane_facebook[follower]['Comments']
        print(f'{follower}: {total_like_and_comments}')


jane_facebook = {}
base_function(jane_facebook)

# test input
# New follower: George
# Like: George: 5
# New follower: George
# Log out
#
# Like: Katy: 3
# Comment: Katy
# New follower: Bob
# Blocked: Bob
# New follower: Amy
# Like: Amy: 4
# Log out