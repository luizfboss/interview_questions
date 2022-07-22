def swapElements(newList):
  pos1 = int(input('Position of first element: '))
  pos2 = int(input('Position of second element: '))

  p1 = newList[pos1 - 1]
  p2 = newList[pos2 - 1]

  temp = newList[pos1 - 1]
  newList[pos1 - 1] = newList[pos2 - 1]
  newList[pos2 - 1] = temp

  return newList

newList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(swapElements(newList))
