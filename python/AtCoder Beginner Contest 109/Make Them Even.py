#奇数だったら左にずらす。
#左にずらせないのであれば、下にずらす
h, w = map(int, input().split())
grid = []
ans = []
for i in range(h):
    grid.append(list(map(int, input().split())))
for i in range(h):
    for j in range(w):
        if grid[i][j] % 2 != 0:
            if j == w - 1:
                if i != h - 1:
                    ans.append([i+1,j+1,i+2,j+1])
                    grid[i+1][j] += 1
            else:
                ans.append([i+1,j+1,i+1,j+2])
                grid[i][j+1] += 1
n = len(ans)
print(n)
for i in ans:
    print("{} {} {} {}".format(i[0], i[1],i[2],i[3]))
