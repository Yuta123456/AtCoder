h,w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
memo = [[None for i in range(w)] for j in range(h)]
memo[h-1][w-1] = False
def check(s,t):
    if (0 <=  s <= h - 1) and (0 <= t <= w - 1):
        return True
    else:
        return False
def calc(y,x):
    if check(y,x) and grid[y][x] != '#':
        if memo[y][x] != None:
            return memo[y][x]
        if calc(y+1,x+1) == False or calc(y,x+1) == False or calc(y+1,x) == False:
            memo[y][x] = True
            return memo[y][x]
        else:
            memo[y][x] = False
            return memo[y][x]
    else:
        return True
calc(0,0)
if memo[0][0]:
    print("First")
else:
    print("Second")
    

        
