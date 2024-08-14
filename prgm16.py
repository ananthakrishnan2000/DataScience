print("SJC23MCA2020 : A S Ananthakrishnan")
print("Batch : MCA 2023-25")
import numpy as np;
A = np.array([[2,1,-2],[3,0,1],[1,-1,-1]])
B = np.array([-3,5,-2])
X = np.linalg.solve(A,B)
print("Matrix A:")
print(A)
print("vector B:")
print(B)
print("solution for X:")
print(X)

