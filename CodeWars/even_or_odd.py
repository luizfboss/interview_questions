# Given a list of integers, determine whether the sum of its elements is odd or even.
# Give your answer as a string matching "odd" or "even".
# If the input array is empty consider it as: [0] (array with a zero).

# Examples:
# Input: [0]
# Output: "even"
# Input: [0, 1, 4]
# Output: "odd"

def odd_or_even(arr):
  return "even" if sum(arr) % 2 == 0 else "odd"

print(odd_or_even([0, 1, 2])) # "odd"
print(odd_or_even([0, 1, 3])) # "even"
print(odd_or_even([1023, 1, 2])) # "even"