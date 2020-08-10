h, w = list(map(int, input().split()))
graph = []
def check(s,t):
    if (0 <=  s <= w - 1) and (0 <= t <= h - 1):
        return True
    else:
        return False
def check_around(x,y):
    if check(x+1,y) and graph[y][x+1] == '#':
        return True
    if check(x,y+1) and graph[y+1][x] == '#':
        return True
    if check(x-1,y) and graph[y][x-1] == '#':
        return True
    if check(x,y-1) and graph[y-1][x] == '#':
        return True
    return False
for i in range(h):
    graph.append(list(input()))
for i in range(h):
    for j in range(w):
        if graph[i][j] == '#':
            if  not check_around(j,i):
                print("No")
                exit()
print("Yes")
            
                
