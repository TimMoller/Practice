spam = ['apples', 'bananas', 'tofu', 88, 'cats']

def stringify(list):
    for i in range(len(list)-1):
        print(list[i], end=', ')
    print('and '+str(list[-1]))

stringify(spam)


# code from stack overflow 
# https://stackoverflow.com/questions/33768758/assigning-any-list-in-a-list-to-string-script
