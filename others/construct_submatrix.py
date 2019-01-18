def construct_submatrix(matrix, rows_to_delete, columns_to_delete):
    
    return matrix

matrix = [[1, 0, 0, 2],
          [0, 5, 0, 1],
          [0, 0, 3, 5]]
rows_to_delete = [1]
columns_to_delete = [0,2]
list_of_tuples = list(zip(*matrix))
list_of_lists = [list(elem) for elem in list_of_tuples]
new_row = [[i for i in row if i != 1] for row in list_of_lists]
print("row: {}".format(new_row))


print("original matrix: {}".format(matrix))
