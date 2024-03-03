key = int(input())
n_lines = int(input())
decrypting_message = []

for _ in range(n_lines):
    message = input()
    decryption = (ord(message)+key)
    decrypting_message.append(chr(decryption))

print(''.join(decrypting_message))
