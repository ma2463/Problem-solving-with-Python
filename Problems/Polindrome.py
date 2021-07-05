# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

def isPolindrome(x: int):
    s = str(x)
    if s == s[::-1]:
        return True
    return False

print(isPolindrome(121))