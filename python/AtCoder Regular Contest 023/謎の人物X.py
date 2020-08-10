r,c,d = map(int, input().split())
grid = []
for i in range(r):
    grid.append(list(map(int, input().split())))
ans = 0
for i in range(r):
    for j in range(c):
        move_count = i + j
        if move_count > d:
            continue
        elif (d - move_count) % 2 == 0:
            ans = max(ans, grid[i][j])
print(ans)

