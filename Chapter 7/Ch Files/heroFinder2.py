import re

heroRegex = re.compile(r'Bat(wo)?man')
mo1 = heroRegex.search('The adventures of Batman')
mo1.group()

mo2 = heroRegex.search('The adventures of Batwoman')
mo2.group()
