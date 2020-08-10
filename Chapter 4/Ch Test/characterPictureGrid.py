                                        # consider lists numbered like this:
grid = [['.', '.', '.', '.', '.', '.'], # grid = [y1[x1,x2,x3,x4,x5,x6],
        ['.', 'O', 'O', '.', '.', '.'], #         y2[x1,x2,x3,x4,x5,x6],
        ['O', 'O', 'O', 'O', '.', '.'], #         y3[x1,x2,x3,x4,x5,x6],
        ['O', 'O', 'O', 'O', 'O', '.'], #         y4[x1,x2,x3,x4,x5,x6],
        ['.', 'O', 'O', 'O', 'O', 'O'], #         y5[x1,x2,x3,x4,x5,x6],
        ['O', 'O', 'O', 'O', 'O', '.'], #         y6[x1,x2,x3,x4,x5,x6],
        ['O', 'O', 'O', 'O', '.', '.'], #         y7[x1,x2,x3,x4,x5,x6],
        ['.', 'O', 'O', '.', '.', '.'], #         y8[x1,x2,x3,x4,x5,x6],
        ['.', '.', '.', '.', '.', '.']] #         y9[x1,x2,x3,x4,x5,x6],]

def rotate(list):
    for x in range(len(list[0])):       # Number of elements in lists contained inside of the list
        for y in range(len(list)):      # Number of elements in the list
            print(list[y][x], end='')   # Print the element in the list from y to x
        print('')                           # so: y1x1 y2x1 y3x1 ...
rotate(grid)
