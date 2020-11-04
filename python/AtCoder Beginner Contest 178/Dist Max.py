n = int(input())
point = []
ans = -1
for i in range(n):
    point.append(list(map(int, input().split())))
x_sub_y = []
x_plus_y = []
for i in range(n):
    x_sub_y.append(point[i][0] - point[i][1])
    x_plus_y.append(point[i][0] + point[i][1])
x_sub_y.sort()
x_plus_y.sort()
ans = max(ans, x_sub_y[-1] - x_sub_y[0], x_plus_y[-1] - x_plus_y[0])
print(ans)