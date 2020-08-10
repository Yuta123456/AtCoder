n, k = map(int, input().split())
x_y = []
x = []
y = []
for i in range(n):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)
    x_y.append([a,b])
ans = 10**19
def check(a,b,c,d):
    count = 0
    for i in range(n):
        s,t = x_y[i]
        if a <= s <= b and c <= t <= d:
            count += 1
    if count >= k:
        return True
    else:
        return False
x.sort()
y.sort()
for x_1 in range(n):
    for x_2 in range(x_1+1,n):
        for y_1 in range(n):
            for y_2 in range(y_1+1,n):
                if check(x[x_1],x[x_2],y[y_1],y[y_2]):
                    rect_area = (x[x_2] - x[x_1]) * (y[y_2] - y[y_1])
                    ans = min(ans, rect_area)
print(ans)
