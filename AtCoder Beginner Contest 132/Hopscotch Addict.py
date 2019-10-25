import numpy as np
n, m = input().split()
data = np.zeros(n,n)
for i in range(m):
    u, v = input().split()
    data[u][v] += 1
s, t = input().split()
