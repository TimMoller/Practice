import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search("My phone number is 412-662-4165.")
print("My phone number is: " + mo.group())
