# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))
# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

def add_binary(a,b):
    return bin(a+b)[2:]


print(add_binary(1,1)) # "10"
print(add_binary(0,1)) # "1"
print(add_binary(1,0)) # "1"
print(add_binary(2,2)) # "100"
print(add_binary(51,12)) # "111111"