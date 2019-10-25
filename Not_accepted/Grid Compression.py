import numpy as np
h, w = list(map(int, input().split()))
ma = []

for i in range(h):
    temp = input()
    if '#' in temp:
        ma.append(temp)
    else:
        h -= 1
ma = np.array(ma)
flag = True
for i in range(w):
    flag = True
    for j in range(h):
        if ma[j][i] == '#':
            flag = False
            break
    if flag:
        np.delete(ma, i, 1)
print(ma)
