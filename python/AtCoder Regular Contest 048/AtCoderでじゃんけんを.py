import bisect
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
rate_acc = [[0,0,0] for i in range(10**5+2)]
for i in range(n):
    r,h = data[i]
    rate_acc[r][h-1] += 1
for i in range(1,10**5+2):
    for j in range(3):
        rate_acc[i][j] += rate_acc[i-1][j]
for i in range(n):
    r,h = data[i]
    win = sum(rate_acc[r-1])
    win += (rate_acc[r][h%3] - rate_acc[r-1][h%3])
    draw = (rate_acc[r][(h-1)] - rate_acc[r-1][(h-1)]) - 1
    print("{} {} {}".format(win,(n-1)-win-draw,draw))
