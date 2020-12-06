import re

heroRegex = re.compile(r'(Ha){3}') ## the {} qualifies the specific number of repetitions
mo1 = heroRegex.search('The adventures of Batman')
mo1.group()

mo2 = heroRegex.search('The adventures of Batwoman')
mo2.group()
