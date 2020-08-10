import numpy as np
h, w, a, b = list(map(int, input().split()))
Ans = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        if ( i < b and j >= a ) or ( i >= b and j < a) :
            Ans[i][j] = 1
for i in range(h):
    print(''.join(list(map(str, Ans[i]))))
