def dont_give_me_five(start, end):
  lista = []
  c = 0
  for n in range(start, end+1):
    lista.append(n)

  for number in lista:
    if number % 5 != 0 and 5 not in number:
      c += 1
  return c

  # return c



print(dont_give_me_five(-17, 9)) # 24 
print(dont_give_me_five(1, 9)) # 8
print(dont_give_me_five(4, 17)) # 12
print(dont_give_me_five(-17, -4)) # 12