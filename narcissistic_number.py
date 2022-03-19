#A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base.
# For example, take 153 (3 digits), which is narcisstic:
    #1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

#and 1652 (4 digits), which isn't:
    #1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
#The Challenge:
#Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10. This may be #True and False in your language, e.g. PHP.

def narcissistic(value):
    arr = []
    string = str(value)
    size = len(string)

    for n in string:
      arr.append(n)

    new_list = map(lambda x: int(x) ** size, arr)

    pre_result = list(new_list)
    result = sum(pre_result)

    if result == value:
      return True
      # f"{value} is narcissistic"
    else:
      return False
      # f"{value} is not narcissistic"


# One-line: 
# def narcissistic(value):
    # return value == sum(int(x) ** len(str(value)) for x in str(value))

print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))