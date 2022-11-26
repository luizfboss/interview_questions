# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.


# FIRST SOLUTION
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    i = 1;
    while True:
        j=(i+x/i)/2.0; # FORMULA USED
        if(abs(i-j) <= 0):
            break;
        i=j;
    return int(j)



# SECOND SOLUTION (BINARY SEARCH):
def mySqrt(self, x):
    l, r = 0, x
    while l <= r:
        mid = l + (r-l)//2
        if mid * mid <= x < (mid+1)*(mid+1):
            return mid
        elif x < mid * mid:
            r = mid - 1
        else:
            l = mid + 1