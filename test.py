A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[4,5,6], [6,7,8], [8,6,7]]
C = [[3,2,3], [5,7,6], [8,7,6]]
import numpy as np
K = np.dot(A,B)
print("(AB)C = {}".format(np.dot(K,C)))

K = np.dot(B,C)

print("A(BC) = {}".format(np.dot(A,K)))