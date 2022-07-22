# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
  if len(arr) > 0:
    return sum([x for x in arr if x > 0])
  return 0


print(positive_sum([1,2,3,4,5])) # 15
print(positive_sum([1,-2,3,4,5])) # 13
print(positive_sum([-1,2,3,4,-5])) # 9
print(positive_sum([-1,-2,-3,-4,-5])) # 0
print(positive_sum([])) # 0