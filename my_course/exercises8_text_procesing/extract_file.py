text_with_extension = input().split('\\')

text_without_extension = text_with_extension[-1].split(".")

print(f"File name: {text_without_extension[0]}")
print(f"File extension: {text_without_extension[1]}")