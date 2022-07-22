#Write a function called repeatStr which repeats the given string string exactly n times.

#repeatStr(6, "I") // "IIIIII"
#repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    return f'{string*repeat}'



print(repeat_str(4, 'a'))
print(repeat_str(3, 'hello '))
print(repeat_str(2, 'abc'))