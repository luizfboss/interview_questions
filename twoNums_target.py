# Given a list and a target, show on the screen the sum of two numbers that match the target.

lista = [1, 2, 3, 4, 5, 6]
target = int(input('Target: '))

for num in range(0, len(lista)):
  for i in range(0, len(lista)):
    if lista[num] + lista[i] == target:
      print(f'{lista[num]}, {lista[i]}')
  