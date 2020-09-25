# bulletPointAdder.py - adds wikipedia points to the beginning
# of each new line on the clipboard.

import pyperclip
text = pyperclip.paste()

#TODO: separate the lines and add the stars
lines = text.split("\n")
for i in range(len(lines)):     # loop through all the indexes in the lined list
    lines[i] = "* " + lines[i]  # add stars to the beginning of each string in the lines list
text = "\n".join(lines)         # join the strings in the lines list
pyperclip.copy(text)            # Copy the updated strings list
