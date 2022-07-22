# Given an integer x, return true if x is palindrome integer.


def isPalindrome(x):
    integer = [num for num in x]
    integer_reverse = integer.reverse()
    if int(x) < 0:
        return False
    elif integer == integer_reverse:
        return True
    else:
        return False



n = '123'
a = '121'
b = '4114'
c = '123'

print(isPalindrome(n))
print(isPalindrome(a))
print(isPalindrome(b))
print(isPalindrome(c))