def matrixElementSum(matrix):
    n = 0
    for row in range(len(matrix)):
        for colum in range(len(matrix[row])):
            if matrix[row][colum]== 0:
                break
            n +=matrix[row][colum]
    
    return n


matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

print(matrixElementSum(matrix))