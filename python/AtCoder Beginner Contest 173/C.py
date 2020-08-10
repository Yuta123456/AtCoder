from itertools import combinations
h,w ,k = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
ans = 0
for row in range(2**h):
    for column in range(2**w):
        grid_a =[[True for i in range(w)] for j in range(h)]
        count = 0
        for p in range(h):
            if (row >> p) & 1:
                for i in range(w):
                    grid_a[p][i] = False
        for p in range(w):
            if (column >> p) & 1:
                for i in range(h):
                    grid_a[i][p] = False
        for i in range(h):
            for j in range(w):
                if grid_a[i][j] and grid[i][j] == '#':
                    count+=1
        if count == k:
            ans += 1
print(ans)


