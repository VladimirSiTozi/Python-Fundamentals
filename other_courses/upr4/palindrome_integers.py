def palindrome(a):
        x = nums
        y = nums[::-1]
        return x == y


numbers = input().split(", ")
for nums in numbers:
    print(palindrome(numbers))