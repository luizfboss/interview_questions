def isPalindrome(x: int) -> bool:
    number = x
    current = 0
    reverseNum = 0
    if x < 9 and x == 0:
        return True

    if x < 0 or x % 10 == 0:
        return False

    
    while reverseNum < x:
        current = number % 10
        reverseNum = reverseNum * 10 + current
        number = number // 10

    if reverseNum == x:
        return True
    else:
        return False


print(isPalindrome(123)) # False
print(isPalindrome(121)) # True
print(isPalindrome(12321)) # True
print(isPalindrome(3441)) # False
print(isPalindrome(3443)) # True
print(isPalindrome(0)) # True