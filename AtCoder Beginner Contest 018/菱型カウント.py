import sys 
input = sys.stdin.readline
r,c,k = map(int, input().split())
grid = []
for i in range(r):
    grid.append(list(input()))
def check(s,t):
    if (0 <= s <= c - 1) and (0 <= t <= r - 1):
        return True
    else:
        return False
up = [[0 for i in range(c)] for j in range(r)]
down = [[0 for i in range(c)] for j in range(r)]
for i in range(c):
    for j in range(r):
        if grid[j][i] == 'o':
            if j == 0:
                up[j][i] = 1
            else:
                up[j][i] = up[j-1][i] + 1
        else:
            up[j][i] = 0
    for j in range(r-1,-1,-1):
        if grid[j][i] == 'o':
            if j == r-1:
                down[j][i] = 1
            else:
                down[j][i] = down[j+1][i] + 1
        else:
            down[j][i] = 0
ans = 0
for i in range(r):
    for j in range(c):
        flag = True
        for wide in range(k):
            if check(j + wide, i) and check(j - wide, i):
                if up[i][j + wide] < k - wide or down[i][j + wide] < k - wide or up[i][j - wide] < k - wide or down[i][j - wide] < k - wide:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            #print("x:{} y:{}".format(j,i))
            ans += 1
print(ans)