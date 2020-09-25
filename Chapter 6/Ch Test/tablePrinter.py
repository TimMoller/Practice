tableData = [['Fruit:', 'apples', 'oranges', 'cherries', 'banana'],
            ['Names:', 'Alice', 'Bob', 'Carol', 'David'],
            ['Animals:', 'dogs', 'cats', 'moose', 'goose']]

# Find the longest str in each of the inner lists
def printTable(table):
    # Create a list with the number of culims as indexes
    colWidth = [0] * len(table)
    # set the colwidth indexes to be the length of the
    # largest string in the list
    for y in range(len(table)):
        for x in table[y]:
            if colWidth[y] < len(x):
                colWidth[y] = len(x)
    # Print out the table with the data from the sublists
    # into columns
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(colWidth[y]), end = ' ')
        print()

printTable(tableData)
