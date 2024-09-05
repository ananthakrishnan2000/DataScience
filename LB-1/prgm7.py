print("SJC23MCA2020 : Ananthakrishnan")
print("batch : MCA 2023-25")

import numpy as np
matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
matrix_sum = matrix1 + matrix2
matrix_diff = matrix1 - matrix2
matrix_prod = matrix1 * matrix2
matrix_div = matrix1 / matrix2
matrix_mul = np.dot(matrix1,matrix2)
matrix_trans = np.transpose(matrix1)
diagonal_sum = np.trace(matrix1)
print("matrix1 :\n",matrix1)
print("matrix2 :\n",matrix2)
print("matrix sum :\n",matrix_sum)
print("matrix difference :\n",matrix_diff)
print("matrix product :\n",matrix_prod)
print("matrix division :\n",matrix_div)
print("matrix multiplication :\n",matrix_mul)
print("transpose:\n",matrix_trans)
print("diagonal sum :\n",diagonal_sum)

