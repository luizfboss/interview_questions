# Your mission, should you accept it, is to return the count of all integers in a given range which do not contain the digit 5 (in base 10 representation).
# You are given the start and the end of the integer range. The start and the end are both inclusive.

# Examples:
# 1,9 -> 1,2,3,4,6,7,8,9 -> return 8
# 4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> return 12

# The start will always be smaller than the end. Both numbers can be also negative.

def dont_give_me_five(start, end):
  lista = []
  c = 0
  for n in range(start, end+1):
    lista.append(n)

  for number in lista:
    if number % 5 != 0 and 5 not in number:
      c += 1
  return c

  # return c



print(dont_give_me_five(-17, 9)) # 24 
print(dont_give_me_five(1, 9)) # 8
print(dont_give_me_five(4, 17)) # 12
print(dont_give_me_five(-17, -4)) # 12