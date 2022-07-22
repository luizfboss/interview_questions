# Find the length of the list and simply swap the first element with the last element.
def swapList(newList):
  size = len(newList)

  temp = newList[0]
  newList[0] = newList[size - 1]
  newList[size - 1] = temp
  
  return newList


lista = [1, 2, 3, 4, 5]
print(swapList(lista))