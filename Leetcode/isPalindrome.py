# First solution

def isPalindrome(self, x):
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



# Second solution - Found on the internet with explanation

# def isPalindrome(self, x: int) -> bool:
        # If x is a negative number it is not a palindrome
        # If x % 10 = 0, in order for it to be a palindrome the first digit should also be 0
        # if x < 0 or (x > 0 and x%10 == 0):   
        #     return False
# 
        # reversedNum = 0

        # while x > reversedNum:
        #     reversedNum = reversedNum * 10 + x % 10
        #     x = x // 10

        # If x is equal to reversed number then it is a palindrome
        # If x has odd number of digits, dicard the middle digit before comparing with x

        # Example, if x = 23132, at the end of for loop x = 23 and reversedNum = 231

        # So, reversedNum/10 = 23, which is equal to x
        # return True if (x == reversedNum or x == reversedNum // 10) else False