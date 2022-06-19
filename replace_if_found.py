# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

list1 = [5, 10, 15, 20, 25, 50, 20]

for i in range(0, len(list1)):
  if list1[i] == 20:
    list1[i] = 200
    break

print(list1)