# You might know some pretty large perfect squares. But what about the NEXT one?
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

# Examples:(Input --> Output)
# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square


from math import sqrt

def find_next_square(sq):
  if sqrt(sq) % 1 == 0:
    nextSq = int(sqrt(sq)) + 1
    return nextSq * nextSq
  return -1

# without using Math library;
# def find_next_square(sq):
#   x = sq**0.5    
#   return -1 if x % 1 else (x+1)**2

print(find_next_square(121)) # "144")
print(find_next_square(625)) # "676")
print(find_next_square(319225)) # "320356")
print(find_next_square(15241383936)) # "15241630849")