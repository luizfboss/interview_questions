def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        # edge cases 
        if len(s) == 0:
            return ""

        string = ""

        for letter in s:
            if letter != " ":
                string += letter

        string = string.lower()
        
        left = 0
        right = len(string)-1

        while right > left:
            if not string[left].isalnum():
                left += 1
                continue
            elif not string[right].isalnum():
                right -= 1
                continue
            else:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
        return True


print(isPalindrome("A man, a plan, a canal: Panama")) # true
print(isPalindrome("race a car")) # false 
print(isPalindrome(" ")) # true