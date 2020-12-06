import re

heroRegex = re.compile(r'Bat(wo)+man') ## the "()+" expression sets the requiremen of at leat one iterance of what's inside the "()+"
mo1 = heroRegex.search('The adventures of Batman')
mo1.group()

mo2 = heroRegex.search('The adventures of Batwoman')
mo2.group()
