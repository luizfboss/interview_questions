def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        """
        Thoughts: 
          - Turn the list of digits into an integer
          - Add one to the integer
          - Turn integer into a list using list compehension
          - Return the new list
        """


        # - Turn the list of digits into an integer
        res = int("".join(map(str, digits)))

        # - Add one to the integer
        res += 1

        # - Turn integer into a list using list compehension
        # - Return the new list
        return [int(x) for x in str(res)]
        


print(plusOne([1,2,3])) # [1,2,4]
print(plusOne([4,3,2,1])) # [4,3,2,2]
print(plusOne([9])) # [1, 0]