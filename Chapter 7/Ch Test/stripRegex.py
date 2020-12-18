#! Python3
# Create a function that stips a chosen string
# If no string is passed to be stripped, strip the white paces.

import re

# Create the stripRegex
stripBlank = re.compile(r" ")

# Create an input sentece for the funtion to strip the wite spaces
test = input("Type a 5 word sentence: ")

# pass the regex through the function
stripBlank.findall(test)
stripTest = 

# output the new sentence
print(stripTest)
