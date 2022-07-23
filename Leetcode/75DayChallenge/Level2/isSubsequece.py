# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

from operator import index


def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    #/charArray = map(lambda x: index(x), t)

   # for char in s:
    #    charArray.append(s.index(char))




initial = "abc"
changed = "ahbgdc"

charArray = [x for x in initial]




print(charArray)



# print(isSubsequence(initial, changed)) # True