# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True

    subsequence=0

    for i in range(0,len(t)):
        if subsequence <= len(s) -1:
            print(s[subsequence])
            if s[subsequence]==t[i]:

                subsequence+=1
    return  subsequence == len(s) 