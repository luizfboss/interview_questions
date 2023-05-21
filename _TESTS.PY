# This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.


def CheckString(string):
    if string.isupper() or string.islower() or string.iscapitalize():
        return True
    else:
        chars = [letter for letter in string]
        if chars[0].isupper() and chars[1:-1].islower():
            return True
    return False


print(CheckString("USA")) # true
print(CheckString("Calvin")) # true
print(CheckString("compUter")) # false
print(CheckString("coding")) # true
