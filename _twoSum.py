# Given a list and a target, show on the screen the sum of two numbers that match the target. 

# FIRST SOLUTION (first try witout worrying about time complexity).
# lista = [1, 2, 3, 4, 5, 6]
# target = int(input('Target: '))
# 
# for num in range(0, len(lista)):
#   for i in range(0, len(lista)):
#     if lista[num] + lista[i] == target:
#       print(f'{lista[num]}, {lista[i]}')



# SOLUTION 2 (MORE OPTIMIZED, WHERE BOTH INDEXES ARE DIFFERENT).
# Time complexity = O(n**2)
# list1 = [1, 2, 3, 9]
# target = 6
# solutions = []
# 
# def twoSum(nums, target):
#    for i in range(len(nums)):
#        for j in range(i+1, len(nums)):
#            if nums[i] + nums[j] == target:
#                return [i, j]
# 
# print(twoSum(list1, target))


# SOLUTION 3 (FASTER THAN SECOND SOLUTION)
# Time Complexity = O(N)
#
# list1 = [1, 2, 3, 9]
# target = 6
# solutions = []
#
# complementMap = Dict()
# for i in range(len(nums)):
#     num = nums[i]
#     complement = target - num
#     if num in complementMap:
#         return [complementMap[num], i]
#     else:
#         complementMap[complement] = i