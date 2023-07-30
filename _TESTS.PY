def removeDuplicates(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  seen = {}
  count = 0
  for i in range(0, len(nums)):
      if nums[i] in seen:
          #remove from the array
          seen[nums[i]] += 1
          nums[i] = "_"

      elif nums[i] not in seen:
          seen[nums[i]] = 1
          count += 1

  for j in range(nums.count("_")):
      nums.remove("_")
      
  return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))