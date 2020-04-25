n,m = map(int, input().split())
ameba = []
delta = [(1,0),(0,1),(-1,0),(0,-1)]
def check(s,t):
    if (0 <=  s <= n - 1) and (0 <= t <= m - 1):
        return True
    else:
        return False
for i in range(n):
    ameba.append(list(map(int, input())))
ans = [[ameba[j][i] for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if ameba[i][j] > 0:
            ans[i+1][j] += ameba[i][j]
            tmp = ameba[i][j]
            for d in delta:
                y = i + d[0] + 1
                x = j + d[1]
                ans[y][x] -= tmp
                ameba[y][x] -= tmp
for i in range(n):
    for j in range(m):
        if ans[i][j] < 0:
            ans[i][j] = 0
for i in range(n):
    print("".join(map(str, ans[i])))

