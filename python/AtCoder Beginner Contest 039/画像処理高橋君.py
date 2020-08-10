h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
ans = [['.' for i in range(w)] for j in range(h)]
#y,x渡すと、(h,w)に入ってるかどうか判定
def check(s,t):
    if (0 <=  s <= h - 1) and (0 <= t <= w - 1):
        return True
    else:
        return False
def check_around(x, y):
    flag = True
    for i in range(-1,2):
        for j in range(-1,2):
            if check(y+i,x+j):
                if grid[y+i][x+j] != '#':
                    flag = False
    if flag:
        ans[y][x] = '#'
def check_ans(x, y):
    flag = False
    for i in range(-1,2):
        for j in range(-1,2):
            if check(y+i,x+j):
                if ans[y+i][x+j] == '#':
                    flag = True
    return flag
        
for i in range(h):
    for j in range(w):
        check_around(j,i)
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            if not check_ans(j,i):
                print("impossible")
                exit()
print("possible")
for i in range(h):
    print("".join(ans[i]))