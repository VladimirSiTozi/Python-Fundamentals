import re

number_of_lines = int(input())
pattern = r'^(\$|\%)([A-Z]{1}[a-z]{2,})\1:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'

for n in range(number_of_lines):
    command = input()
    match = re.findall(pattern, command)
    if not match:
        print('Valid message not found!')
    else:
        given_word = match[0][1]
        letter1 = int(match[0][2])
        letter2 = int(match[0][3])
        letter3 = int(match[0][4])
        message = chr(letter1) + chr(letter2) + chr(letter3)
        print(f'{given_word}: {message}')

# test input
# 4
# $Request$: [73]|[115]|[105]|
# %Taggy$: [73]|[73]|[73]|
# ggy%: [118]|[97]|[108]|
# $Request$: [73]|[115]|[105]|[32]|[75]|

# 3
# This shouldnt be valid%Taggy%:
# [118]|[97]|[108]|
# $tAGged$: [97][97][97]|
# $Request$: [73]|[115]|[105]|true