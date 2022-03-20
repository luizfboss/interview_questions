# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

def remove_char(s):
    if len(s) <= 2:
      return ''
    else:
      string = [char for char in s]
      string.remove(string[0])
      string.remove(string[-1])
      new_string = ''.join(letter for letter in string)
      return new_string

# One-line solution: return s[1 : -1]

print(remove_char('eloquent')) # 'loquen'
print(remove_char('country')) # 'ountr'
print(remove_char('person')) # 'erso'
print(remove_char('place')) # 'lac'
print(remove_char('ok')) # ''
print(remove_char('ooopsss')) # 'oopss'
