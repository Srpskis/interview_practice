

def zero_matrix(matrix, row, column):
    dicti = {}
    key = 0

    for i in range (0, row):
        for j in range(0, column):
            if matrix[i][j] == 0:
                l = [i, j]
                dicti[key] = l
                key += 1

    for key, value in dicti.items():
        r = dicti[key][0]
        c = dicti[key][1]

        for i in range(0, column):
            matrix[r][i] = 0

        for i in range(0, row):
            matrix[i][c] = 0

matrix =    [   [1,1,1,1,1],
                [1,0,1,0,1],
                [1,1,1,1,1],
                [1,0,1,1,1]
            ]

row = 4
col = 5
print(matrix)
zero_matrix(matrix, row, col)
print(matrix)

