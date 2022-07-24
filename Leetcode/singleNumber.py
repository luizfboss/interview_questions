# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# SOLUTION 1 - BY MYSELF USING COUNT METHOD
def singleNumber(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num


# SOLUTION 2 - FOUND ON THE INTERNET
def singleNumber(nums: list[int]) -> int:
    sol = 0
    for b in nums:
        sol ^= b
    
    return sol


# SOLUTION 3 - FOUND ON THE INTERNET
def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        
        for j in nums:
            if j not in dic:
                dic[j] = 1
            
            else:
                dic[j] +=1
        
        for j in dic:
            if dic[j] == 1:
                return j


# SOLUTION 4 - FOUND ON THE INTERNET (SOLUTION WITH ARRAYS)
def singleNumber(nums: list[int]) -> int:
	tmp = []
	for num in nums:
		if num in tmp:
			tmp.remove(num)
		else:
			tmp.append(num)
	return tmp[0]