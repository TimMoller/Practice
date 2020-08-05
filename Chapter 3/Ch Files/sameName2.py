def spam():
    global eggs     # eggs is declared as the global var
    eggs = 'spam'   # 'spam' set as the global var as per above

eggs = 'global'
spam()
print(eggs)
