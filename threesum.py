# Find three numbers that sums up to 0.
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

def threeSum(nums):
  """
  :type nums: List[int]
  :rtype: List[List[int]]
  """
  count = 0
  res = []
  curr = []

  if len(nums) == 0:
    return []

  for a in nums:
    for b in nums:
      for c in nums:
        if sum([a, b, c]) == 0:
          current = [a, b, c]
          res.append(current)
  return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))