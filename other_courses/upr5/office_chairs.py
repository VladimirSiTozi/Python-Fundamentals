number_of_rooms = int(input())
chairs_left = 0
game_on_checker = True

for rooms in range(number_of_rooms):
    chairs_and_visitors = input().split()
    chairs = chairs_and_visitors[0]
    visitors = int(chairs_and_visitors[1])

    if len(chairs) > visitors:
        chairs_left += len(chairs) - visitors

    elif len(chairs) < visitors:
        more_chairs_needed = visitors - len(chairs)
        print(f"{more_chairs_needed} more chairs needed in room {rooms + 1}")
        game_on_checker = False

if game_on_checker:
    print(f"Game On, {chairs_left} free chairs left")


# test input()
# 4
# XXXX 4
# XX 1
# XXXXXX 3
# XXX 3

# 3
# XXXXXXX 5
# XXXX 5
# XXXXXX 8