text = input().split()
palindrome = input()
text_palindromes = [word for word in text if word == word[::-1]]
print(text_palindromes)

matched_palindromes = [word for word in text_palindromes if word == palindrome]
print(f'Found palindrome {len(matched_palindromes)} times')

# test input
# hey how you doin? lol
# mom
#
# wow father mom wow shirt stats
# wow