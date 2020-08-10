import sys
sys.setrecursionlimit(10**6)
h,w = map(int, input().split())
grid = []
mod = 10**9+7
for i in range(h):
    grid.append(list(map(int, input().split())))
dp = [[-1 for i in range(w)] for j in range(h)]
ans = 0
def check(s,t):
    if (0 <=  s <= h - 1) and (0 <= t <= w - 1):
        return True
    else:
        return False
def calc(x,y):
    if dp[y][x] != -1:
        return dp[y][x]
    delta = [(-1,0),(0,1),(1,0),(0,-1)]
    path = 1
    for d in delta:
        if check(y+d[0],x+d[1]):
            if grid[y][x] > grid[y+d[0]][x+d[1]]:
                path += calc(x+d[1],y+d[0])
    dp[y][x] = path % mod
    return path


for i in range(h):
    for j in range(w):
        ans += calc(j,i)
print(ans%mod)



