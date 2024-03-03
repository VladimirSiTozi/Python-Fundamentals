text = input()
new_text = ''

for ch in text:
    new_ch = ord(ch) + 3
    new_text += chr(new_ch)

print(new_text)