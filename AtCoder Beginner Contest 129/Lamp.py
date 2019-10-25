h, w = map(int,input().split())
grid = []
for i in range(h):
    grid.append(list(map(int, input().split())))
L = [[0 for i in range(h)] for j in range(w)]
R = [[0 for i in range(h)] for j in range(w)]
U = [[0 for i in range(h)] for j in range(w)]
D = [[0 for i in range(h)] for j in range(w)]
for i in range(h):
    for j in range(w):
        if grid[i][j] ==  ".":
            if i == 0:
                
        else:
            L[i][j] = 0
            R[i][j] = 0
            U[i][j] = 0
            D[i][j] = 0
