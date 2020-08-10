from collections import deque
h, w = list(map(int, input().split()))
grid = []
for i in range(h):
    grid.append(list(input()))
#x,y渡すと、（h,w）に入ってるかどうか判定
def check(s,t):
    if (0 <=  s <= h - 1) and (0 <= t <= w - 1):
        return True
    else:
        return False
ans = [[0 for i in range(w)] for j in range(h)]
#graph => そこまでの距離を保存した二次元配列　grid=>与えられた迷路
ans[0][0] = 1
mod = 10**9+7
for i in range(h):
    for j in range(w):
        if grid[i][j] != '#':
            if i - 1 >= 0:
                ans[i][j] += ans[i-1][j]
            if j - 1 >= 0:
                ans[i][j] += ans[i][j-1]
        else:
            ans[i][j] = 0
        ans[i][j] %= mod
print(ans[-1][-1])