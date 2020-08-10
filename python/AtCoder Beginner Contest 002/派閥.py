import itertools
n, m = map(int, input().split())
graph = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
for i in range(n+1):
    graph[i][i] = 1
#bit_search
ans = 1
cand = list(itertools.product([0,1], repeat=n))
def check(li):
    team = []
    res = 0
    for i in range(len(li)):
        if li[i] == 1:
            res += 1
            team.append(i+1)
    #出来上がったチームに対して、可能かどうかを判定する
    for i in team:
        for j in team:
            if graph[i][j] == 0:
                return 1
    return res
for i in cand:
    ans = max(check(i), ans)
print(ans)
