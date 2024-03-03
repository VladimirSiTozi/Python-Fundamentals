text1, text2 = input().split()
total_sum = 0

if len(text1) > len(text2):
    for index in range(len(text2)):
        total_sum += ord(text1[index]) * ord(text2[index])
    for index in range(len(text2), len(text1)):
        total_sum += ord(text1[index])
elif len(text2) > len(text1):
    for index in range(len(text1)):
        total_sum += ord(text1[index]) * ord(text2[index])
    for index in range(len(text1), len(text2)):
        total_sum += ord(text2[index])
else:
    for index in range(len(text1)):
        total_sum += ord(text1[index]) * ord(text2[index])

print(total_sum)