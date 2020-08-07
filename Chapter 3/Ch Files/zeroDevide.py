def spam(divideBy):
    try:                                    # if conditions met return the following argument
        return 42 / divideBy
    except ZeroDivisionError:               # if the code reveals an error, print the following statement.
        print('Error: Invalid argument.')


print(spam(16))
print(spam(6))
print(spam(0))
print(spam(84))
