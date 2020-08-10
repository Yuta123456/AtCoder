from itertools import combinations
def calc_triangle_area(x_1,y_1,x_2,y_2,x_3,y_3):
    return abs((x_1 - x_3) * (y_2 - y_3) - (x_2 - x_3)*(y_1 - y_3))
n = int(input())
data = []
ans = 0
for i in range(n):
    data.append(list(map(int, input().split())))
for (a,b,c) in combinations(range(0,n), 3):
    area = calc_triangle_area(data[a][0], data[a][1], data[b][0], data[b][1], data[c][0], data[c][1])
    if area % 2 == 0 and area != 0:
        ans += 1
print(ans)