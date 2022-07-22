# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.




# First solution (worked perfectly): 
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """

    for n in nums:
        if target == n:
            return True
    return False


print(search([2,5,6,0,0,1,2], 0))
print(search([2,5,6,0,0,1,2], 4))
print(search([2,5,6,0,0,1,2], 5))



# SOLUTION 2 - FOUND ON THE INTERNET (BINARY SEARCH ALGORITHM)

# Note: Since duplicate elemnts are present in the array so remove all the duplicates before step step 1.
# To remove duplicate:
# Shift left while left == left+1, and
# Shift right while right == right-1.
# If the length of the given array list is 1, then check the first element and return accordingly
# if len(nums)==1:
#     if nums[0]!=target:
#         return False
#     else:
#         return True
# 
# left=0
# right=len(nums)-1
# # binary search 
# while(left<=right):
# 
#     # shifting to remove duplicate elements
#     while left<right and nums[left] == nums[left+1]:
#         left+=1
#     while left<right and nums[right] == nums[right-1]:
#         right-=1
# 
#     # step 1 calculate the mid    
#     mid=(left+right)//2
# 
#     #step 2
#     if nums[mid]==target:
#         return True
# 
#     #step 3
#     elif nums[left]<=nums[mid]:
#         if nums[mid]>=target and nums[left]<=target:
#             right=mid-1
#         else:
#             left=mid+1
# 
#     # step 4
#     else:
#         if target>=nums[mid] and target<=nums[right]:
#             left=mid+1
#         else:
#             right=mid-1
# 
# # step 5
# return False