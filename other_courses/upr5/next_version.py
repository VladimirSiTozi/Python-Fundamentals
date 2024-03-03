version = [int(num) for num in input().split(".")]
version[-1] += 1
for index in range(len(version)-1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        if index - 1 >= 0:
            version[index-1] += 1

version = [str(num) for num in version]
print('.'.join(version))

# test input
# 1.2.3
#
# 1.3.9
#
# 3.9.9