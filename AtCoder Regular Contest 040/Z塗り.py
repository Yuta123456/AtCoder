n = int(input())
grid = []
ans = 0
for i in range(n):
    grid.append(list(input()))
for i in range(n):
    if '.' in grid[i]:
        ans += 1
        last_index = -1
        for j in range(n):
            if grid[i][j] == '.':
                grid[i][j] = 'o'
                last_index = j
        for j in range(last_index,n):
            if i + 1 < n:
                grid[i+1][j] = 'o'
print(ans)