# Given an array, reverse it.
lista = [1, 2, 3, 4, 5]
newLista = []

for i in range(1, len(lista)+1):
  newLista.append(lista[-i])

print(f'Reversed list: {newLista}')

# print(list(reversed(lista)))