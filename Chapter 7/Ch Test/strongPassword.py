#! python3
# create a function that tests the strength of a password:

import pyperclip, re

# Create regex:
capitalTestRegex = re.compile(r"([A-Z])")
specialTestRegex = re.compile(r"([,.!@#$%*+-])")
numberTestRegex = re.compile(r"([0-9])")

# Test that password is at least 8 characters long:
password = str(pyperclip.paste())
if len(password) < 8:
    print("not enough characters, must be at least 8 characters long")
else:
    print(password)

# search for Upper and lower case, numbers and special characters:
if capitalTestRegex.search(password) == None:
    print("Password must contain at least one Capital Letter.")
elif specialTestRegex.search(password) == None:
    print("password must contain at least one special character.")
elif numberTestRegex.search(password) == None:
    print("Password must contain at leat one number")
else:
    print("Password Looks good!")

# Test that there is at least 1 Upper case character AND special character:
