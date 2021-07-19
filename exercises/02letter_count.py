# Write a function called `letter_count` to count the letter
# occurrence in a string. Use a dictionary.
#
# You can iterate over a string one letter at a time using
# a for loop.
#
# for letter in "alpha":
#   print(letter)
#
# Create a dictionary with `dd = {}`. Assign values with `dd["foo"] = 1`.
# Check to see if a dictionary has a key using the `in` operator.
#
# dd = {}
# dd["foo"] = 1
# dd["foo"] += 1
# if "foo" in dd:
#   print(dd["foo"])
#
# Careful. Python requires that you insert a key into a dictionary
# before you try to modify it's value. If you try to access a dictionary
# at a key that hasn't been added you'll get an error and the program will
# crash. Remember to use an if statement to see if a key is "in" a dictionary
# before you try to read it!
#
# d2 = {}
# d2["foo"]
# > KeyError: 'foo'
#
# Example function call:
#
# letter_count('banana')
#
# > {'a': 3, 'b': 1, 'n': 3}

def letter_count(string):
  new_dict = {}
  for letter in string:
    new_dict[letter] = string.count(letter) 
    # or getter
                            # .get(letter, 0) + 1
# if letter not in new_dict:
  # new_dict[letter] = 1
  # else:
  #   new_dict[letter] = new_dict[letter_count] + 1
  return new_dict 
  
print(letter_count('banana'))