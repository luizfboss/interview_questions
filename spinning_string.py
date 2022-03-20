# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples: 
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
  list_string = sentence.split(' ')
  new_list = []
  for w in list_string:
    if len(w) > 4:
      new_list.append(w[::-1])
    else:
      new_list.append(w)
  return ' '.join(new_list)

# Single Words
print(spin_words("Welcome")) # "emocleW"
print(spin_words("to")) # "to"
print(spin_words("CodeWars")) # "sraWedoC"
# Multiple Words
print(spin_words("Hey fellow warriors")) # "Hey wollef sroirraw"
print(spin_words("This sentence is a sentence")) # "This ecnetnes is a ecnetnes"