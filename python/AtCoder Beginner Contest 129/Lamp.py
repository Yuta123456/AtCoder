h, w = map(int,input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
L = [[0 for i in range(w)] for j in range(h)]
R = [[0 for i in range(w)] for j in range(h)]
U = [[0 for i in range(w)] for j in range(h)]
D = [[0 for i in range(w)] for j in range(h)]
#Uを決める
for i in range(w):
    if grid[0][i] == '#':
        U[0][i] = 0
    else:
        U[0][i] = 1
for i in range(1,h):
    for j in range(w):
        if grid[i][j] == '#':
            U[i][j] = 0
        else:
            U[i][j] = U[i-1][j] + 1
 #Dを決める
for i in range(w):
    if grid[-1][i] == '#':
        D[-1][i] = 0
    else:
        D[-1][i] = 1
for i in range(h-2, -1,-1):
    for j in range(w):
        if grid[i][j] == '#':
            D[i][j] = 0
        else:
            D[i][j] = D[i+1][j] + 1
# R を決める
for i in range(h):
    if grid[i][-1] == '#':
        R[i][-1] = 0
    else:
        R[i][-1] = 1
for i in range(h):
    for j in range(w-2,-1,-1):
        if grid[i][j] == '#':
            R[i][j] = 0
        else:
            R[i][j] = R[i][j+1] + 1
#Lを決める
for i in range(h):
    if grid[i][0] == '#':
        L[i][0] = 0
    else:
        L[i][0] = 1
for i in range(h):
    for j in range(1,w):
        if grid[i][j] == '#':
            L[i][j] = 0
        else:
            L[i][j] = L[i][j-1] + 1
ans = 0
for i in range(h):
    for j in range(w):
        #print("x:{} y:{} L:{} R:{} U:{} D:{}".format(j+1,i+1,L[i][j],R[i][j],U[i][j],D[i][j]))
        ans = max(ans, L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3)
print(ans)