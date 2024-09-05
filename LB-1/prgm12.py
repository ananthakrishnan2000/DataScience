print("SJC23MCA-2020 : Ananthakrishnan")
print("batch : MCA 2023-25")
import numpy as np
X = np.array([[1,2],
              [3, 4]])
y = np.random.rand(*X.shape)
result = X * 2 + 2 * y
print(result)
