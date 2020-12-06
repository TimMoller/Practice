import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall("Hello there my name is Timothy.")

consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall("hello there my name is Timothy Moller.")
