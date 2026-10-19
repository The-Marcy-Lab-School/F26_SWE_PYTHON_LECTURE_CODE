letters = ['a', 'b', 'c', 'd', 'e']

letters.append('f')      # adds 'f' to the end of letters
letters.insert(0, 'z')   # adds 'z' to the beginning of letters
print(letters)  # Prints ['z', 'a', 'b', 'c', 'd', 'e', 'f']

letters.pop()    # removes the last element ('f')
letters.pop(0)   # removes the first element ('z')
print(letters)  # Prints ['a', 'b', 'c', 'd', 'e']

letters.insert(2, 'Hi!')  # At index 2, inserts 'Hi!'
print(letters)  # Prints ['a', 'b', 'Hi!', 'c', 'd', 'e']

letters[2] = 'Hey ;)'  # At index 2, replaces 1 element with 'Hey ;)'
print(letters)  # Prints ['a', 'b', 'Hey ;)', 'c', 'd', 'e']

letters.remove('Hey ;)')  # Removes the first 'Hey ;)' it finds
print(letters)  # Prints ['a', 'b', 'c', 'd', 'e']
