h,w = map(int, input().split())
grid = []
#二次元累積和。
def da_generate(h,w,a):
    da = [[0]*w for j in range(h)]
    if a[0][0] == 'o':
        da[0][0] = 1
    else:
        da[0][0] = 0
    for i in range(1,w):
        if a[0][i] == 'o':
            da[0][i] = da[0][i-1]+1
    for i in range(1,h):
        cnt_w = 0
        for j in range(w):
            if a[i][j] == 'o':
                cnt_w += 1
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
for i in range(h):
    grid.append(list(input()))
graph = da_generate(h,w,grid)
a_ans = 0
b_ans = 0
c_ans = 0
i = 0
j = 0
k = 0
while i < h:
    j = 0
    while j < w:
        k = 1
        while k < 21:
            if i + 7*k > h or j + 7*k > w:
                break
            rect = da_calc(i,j,i+7*k-1, j+7*k-1, graph)
            print(rect)
            if rect == 12 * (k**2):
                a_ans += 1
            elif rect == 16 * (k**2):
                b_ans += 1
            elif rect == 11 * (k**2):
                c_ans += 1
            k += 1
        j += 1
    i += 1
print("{} {} {}".format(a_ans,b_ans,c_ans))


