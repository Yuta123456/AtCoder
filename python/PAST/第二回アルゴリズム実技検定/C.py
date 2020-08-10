n = int(input())
grid = []
for i in range(n):
    grid.append(list(input()))
for i in range(n-2,-1,-1):
    for j in range(1,2*n-2):
        if grid[i][j] == '#':
            if grid[i+1][j-1] == 'X' or grid[i+1][j] == 'X' or grid[i+1][j+1] == 'X':
                grid[i][j] = 'X'
for i in range(n):
    print("".join(grid[i]))
    
