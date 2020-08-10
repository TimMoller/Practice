spam = ['apples', 'bananas', 'tofu', 'trebble cleff', 17, 'cats']

def stringify(list):
    for i in range(len(list)-1):
        print(list[i], end=", ")  # the 'end=' parameter carries on the code on the same line instead of a  new line
    print('and ' + str(list[-1]))
stringify(spam)
