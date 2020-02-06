n = int(input())
point = []
def da_generate(h,w,a):
    da = [[0]*w for j in range(h)]
    da[0][0] = a[0][0]
    for i in range(1,w):
        da[0][i] = da[0][i-1]+a[0][i]
    for i in range(1,h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]
            da[i][j] = da[i-1][j]+cnt_w
    return da
#da_calc(p,q,x,y):(p,q)~(x,y)の長方形の和
def da_calc(p,q,x,y,da):
    if p > x or q > y:
        return 0
    if p == 0 and q == 0:
        return da[x][y]
    if p == 0:
        return da[x][y]-da[x][q-1]
    if q == 0:
        return da[x][y]-da[p-1][y]
    return da[x][y]-da[p-1][y]-da[x][q-1]+da[p-1][q-1]
import sys
input = sys.stdin.readline
for i in range(n):
    point.append(list(map(int, input().split())))
p = int(input())
area = [[1 for i in range(n)] for j in range(n)]
point = da_generate(n,n,point)
area = da_generate(n,n,area)
#preprocess
area_point = [0 for i in range(n*n+1)]
for x_1 in range(n):
    for y_1 in range(n):
        for x_2 in range(x_1,n):
            for y_2 in range(y_1, n):
                k = da_calc(x_1, y_1, x_2, y_2, area)
                area_point[k] = max(area_point[k], da_calc(x_1,y_1,x_2,y_2,point))
for i in range(1,n*n):
    area_point[i] = max(area_point[i-1], area_point[i])
for i in range(p):
    q = int(input())
    print(area_point[q])