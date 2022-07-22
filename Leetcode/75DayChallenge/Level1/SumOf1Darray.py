# Find the sum of the 1D Array

def runningSum(nums):
    curr = 0
    arr = []
    for num in nums:
        curr += num
        arr.append(curr)
    
    return arr

print(runningSum([1, 1, 1, 1, 1]))