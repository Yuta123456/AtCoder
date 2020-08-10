n,m,x = map(int, input().split())
data = []
for i in range(n):
    a = list(map(int, input().split()))
    data.append([a[0],a[1:]])
ans = 10**18
for i in range(pow(2,n)):
    i = list(("{:b}".format(i).zfill(n)))
    cost = 0
    learn = [0 for i in range(m)]
    for index,flag in enumerate(i):
        if int(flag):
            for j in range(m):
                learn[j] += data[index][1][j]
            cost += data[index][0]
    flag = True
    for j in range(m):
        if learn[j] < x:
            flag = False
    if flag:
        ans = min(ans, cost)
if ans == 10**18:
    print(-1)
else:
    print(ans)


