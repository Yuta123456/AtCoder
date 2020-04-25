n,a,b = map(int, input().split())
point = []
for i in range(n):
    point.append(int(input()))
p = max(point) - min(point)
if p == 0:
    #?
    if a == point[0] and b == 0:
        print("{} {}".format(1,0))
    else:
        print(-1)
        exit()
else:
    p = b / p
q = (a*n - sum(point) * p) / n
print("{} {}".format(p,q))