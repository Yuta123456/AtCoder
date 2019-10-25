import numpy as np

k = int(input())
R = []
length = 2**k

def win(x, y):
    return 1 / (1 + 10 ** ((y - x) / 400))

for i in range(length):
    R.append(int(input()))
table =  np.zeros((length, length) ,dtype = 'float')
dp = np.zeros((k + 1, length) ,dtype = 'float')
for i in range(length):
    for j in range(i+1, length):
        table[i][j] = win(i, j)
        table[j][i] = 1 - table[i][j]
for i in range(length):
    dp[0][i] == 1
for i in range(k + 2):
    for j in range(length):
        for 
