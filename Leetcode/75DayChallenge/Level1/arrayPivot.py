# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.


# FIRST SOLUTION - ALL BY MYSELF

def pivotIndex(nums):
    # split array in two 
    # get index from for loop
    # sum both arrays, and see if they match. 
    # Remove the number which index is the one to be returned (sum(arr) - nums[i])
    for i in range(len(nums)):

        arr1 = nums[:i]
        arr2 = nums[i:]

        if sum(arr1) == sum(arr2) - nums[i]:
            return i
    return -1

print(pivotIndex([1,7,3,6,5,6])) # 3
print(pivotIndex([1,2,3])) # -1 (does not exist)