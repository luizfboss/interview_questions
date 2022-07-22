# Exercise 5: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for c in range(0, len(list1)):
  print(f"{list1[c]} {list2[-(c+1)]}")