h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
ans = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == '.':
            if j + 1 < w and grid[i][j+1] == '.':
                ans += 1
            if i + 1 < h and grid[i+1][j] == '.':
                ans += 1
print(ans)