# Given a list and a target, show on the screen the sum of two numbers that match the target. 

# FIRST SOLUTION
# lista = [1, 2, 3, 4, 5, 6]
# target = int(input('Target: '))
# 
# for num in range(0, len(lista)):
#   for i in range(0, len(lista)):
#     if lista[num] + lista[i] == target:
#       print(f'{lista[num]}, {lista[i]}')



# SOLUTION 2 (MORE OPTIMIZED, WHERE BOTH INDEXES ARE DIFFERENT).
# list1 = [1, 2, 3, 9]
# target = 6
# solutions = []
# 
# def sum_target(arr: list):
#   for a in range(0, len(list1)):
#     for b in range(1, len(list1)):
#       if a != b:
#         if list1[a] + list1[b] == target:
#             print(f"{list1[a]} and {list1[b]} match the target!")
#             return True
#   return False
# 
# print(sum_target(list1))