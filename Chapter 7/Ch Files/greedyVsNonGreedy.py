import re

greedyRegex = re.compile(r'(Ha){3,5}') ## make sure there are no spaces in the {}
mo1 = greedyRegex.search("HaHaHaHaHa")
mo1.group()

nonGreedyRegex = re.compile(r'(Ha){3,5}?') ## make sure there are no spaces in the {}
mo2 = nonGreedyRegex.search("HaHaHaHaHa")
mo2.group()
