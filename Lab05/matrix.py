matrix = [[2, 3, 5],
          [4, 3, 1],
          [0, 9, 3]]

# =============================================================================
# matrix[2][0] 
# matrix[0][2]  
# matrix[0][0:2]  
# matrix[:, 0]  
# matrix[1][::-1]
# matrix[::2][1:2]
# =============================================================================

vector = [6, 7, 8]

matrix_product = []
for i in range(len(matrix)):
    row_sum = 0
    for j in range(len(vector)):
        row_sum += vector[j] * matrix[i][j]

    matrix_product.append(row_sum)
