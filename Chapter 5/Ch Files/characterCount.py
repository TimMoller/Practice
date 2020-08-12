message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0) # the .setdefault(k,v) method prevents a KeyError
    # if the character is not in the dictionary
    # the character is set as the key and the value is defaulted to 0
    count[character] = count[character] + 1
    # when a character appears the dictionary is updated.
    # the firs instance of a key add 1 to the value
    # if the key reappears in the loop, 1 is added again

print(count)
