# The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

def open_or_senior(data):
  arr = []
  category = ''
  handicap = ''
  for sub_arr in data:
    if sub_arr[0] >= 55 and sub_arr[1] > 7:
          category = 'Senior'
          arr.append(category)
    else: 
      category = 'Open'
      arr.append(category)
  return arr

# One-line solution: 
# def openOrSenior(data):
#     return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])) # ['Open', 'Senior', 'Open', 'Senior']
print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)])) # ['Open', 'Open', 'Senior', 'Open']