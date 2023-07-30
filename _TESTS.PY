def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    seen = {}

    for num in nums:
        if num not in seen:
            seen[num] = 1
        elif num in seen:
            seen[num] += 1

    seen_keys = list(seen.keys())
    result = list(seen.values()).index(1)

    return seen_keys[result]

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))
