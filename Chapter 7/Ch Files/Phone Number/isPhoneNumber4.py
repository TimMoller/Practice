import re

# grouping the regular espressions with Parenthese
# taking the regular expression you can create a more advanced search
# and reacall
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My phone number is 412-662-4165.")
print("My phone number is: " + mo.group())

# recall the first grouping
print(mo.group(1))
# recall the second grouping
print(mo.group(2))
# recall the full set of groups
print(mo.group(0))
