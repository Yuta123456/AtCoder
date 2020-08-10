n = int(input())
x_count = 0
flag = [[False for i in range(n+2)] for j in range(n+2)]
ans = [['.' for i in range(n+2)] for j in range(n+2)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i % 5 == 1 and j % 5 == 2) or (i % 5 == 2 and j % 5 == 4) or (i % 5 == 3 and j % 5 == 1) or (i % 5 == 4 and j % 5 == 3) or (i % 5 == 0 and j % 5 == 0):
            ans[i][j] = 'X'
            flag[i][j] = True
            flag[i][j+1] = True
            flag[i+1][j] = True
            flag[i][j-1] = True
            flag[i-1][j] = True
for i in range(1,n+1):
    for j in range(1,n+1):
        if not flag[i][j]:
            ans[i][j] = 'X'
            flag[i][j] = True
            flag[i][j+1] = True
            flag[i+1][j] = True
            flag[i][j-1] = True
            flag[i-1][j] = True
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{}".format(ans[i][j]), end="")
    print()