spam = ['apples', 'bananas', 'tofu', 'trebble cleff', 'cats']

def stringify(list):
    string = ""
    for i in list[:-1]:
        if i not in string:
            string += i + ", "
    for i in list[-1:]:
        if i not in string:
            string += "and " + i

    print(string)

stringify(spam)
