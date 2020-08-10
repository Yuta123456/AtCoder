from copy import deepcopy
grid = []
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]
par = [-1]*100
circle_count = 0
for i in range(10):
    grid.append(list(input()))
    circle_count += grid[i].count('o')
delta = [(-1,0), (1,0), (0,1),(0,-1)]
#init
for row in range(10):
    for column in range(10):
        if grid[row][column] == 'o':
            for d in delta:
                y = row + d[0]
                x = column + d[1]
                if 0 <= y < 10 and 0 <= x < 10 and grid[y][x] == 'o':
                    unite(10*row+column, 10*y+x)
original_uf = deepcopy(par)
for row in range(10):
    for column in range(10):
        par = deepcopy(original_uf)
        for d in delta:
            y = row + d[0]
            x = column + d[1]
            if 0 <= y < 10 and 0 <= x < 10 and grid[y][x] == 'o':
                unite(10*row+column, 10*y+x)
        if size(10*row+column) == circle_count+1:
            print("YES")
            exit()
print("NO")