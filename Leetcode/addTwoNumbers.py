#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# list1 = [2,4,3]
# list2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# FIRST SOLUTION - BY MYSELF (DID NOT WORK ON LEETCODE, BUT HERE IT WORKED PERFECTLY)
# def addTwoNumbers(l1, l2):
#   s1 = 0
#   s2 = 0
# 
#   for i, num in enumerate(l1):
#     s1 = s1 + (num * (10 ** i))
# 
#   for i, num in enumerate(l2):
#     s2 = s2 + (num * (10 ** i))
# 
#   res = s1 + s2
# 
#   return res
# 
# 
# print(addTwoNumbers(list1, list2))


# SOLUTION 2: O(N) time and O(1) space.

# def addTwoNumbers(l1, l2):
#   if not l1:
#       return l2
#   if not l2:
#       return l1
# 
#   head = l1
#   prev = l1
#   carry = 0
#   while l1 or l2:
#       
#       sum_ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
#       carry = sum_//10
#       sum_ = sum_%10
#       if l1:
#           l1.val = sum_
#           prev = l1
#           l1 = l1.next
#       else:
#           newNode = ListNode(sum_, None)
#           prev.next = newNode
#           prev = prev.next
#           
#       if l2:
#           l2 = l2.next
#           
#   if carry == 1:
#       newNode = ListNode(carry, None)
#       prev.next = newNode
#       prev = prev.next
#           
#   return head