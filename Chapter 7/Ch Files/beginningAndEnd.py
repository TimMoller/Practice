import re

beginningRegex = re.compile(r'^\d$') ## remember to use the back-slash!!
mo1 = beginningRegex.search("01234567890")
