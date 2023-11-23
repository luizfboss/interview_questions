def merge(nums1: [int], m: int, nums2: [int], n: int):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    length_new_list = m + n
    nums1 = list(filter(lambda x: x != 0, nums1))

    # get pointer for buth lists (nums1 and nums2)
    nums1_index = 0
    nums1_p = nums1[nums1_index]

    nums2_index = 0
    nums2_p = nums2[nums2_index]
    len_nums2 = len(nums2)
    

    counter = 0
    while counter < len(nums1):
        # compare nums2_p to current nums1_p. if nums2_p is less than nums1_p, insert it in nums1
        if nums2_p <= nums1_p:
            nums1.insert(nums2_p, nums1_index)
            # remove element from nums2 and decrement len_nums2 by one
            nums2.remove(nums2_p)
            # len_nums2 -= 1
        # end of for loop - increment 1 to nums1_index
        len_nums2 -= 1
        nums1_index += 1

    # append remaining elements from nums2
    if len_nums2 != 0:
        for j in range(0, len_nums2):
            nums1.append(nums2[j])
    
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))