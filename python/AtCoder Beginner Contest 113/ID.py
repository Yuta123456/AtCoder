n, m = list(map(int, input().split()))
data = []
for i in range(m):
    data.append([i + 1] + list(map(int, input().split())))
    #data[0::] = cityNumber,
    #data[:0:] = prefect,
    #data[::0] = year
data = sorted(data, key = lambda x: (x[1], x[2]))
#prefect => year
ans = [[0,0,0] for i in range(m)]
#ans[::0] = city Number
#ans[0::] = prefect
#ans[:0:] = ID

pre = data[0][1]
num = 0
for i in range(m):
    ans[i][0] = data[i][1] # prefect
    ans[i][2] = data[i][0] #cityNumber
    if pre == data[i][1]:
        num += 1
    else:
        num = 1
    ans[i][1] = num
    pre = data[i][1]
ans = sorted(ans, key = lambda x:x[2])
for i in range(m):
    print("{:0=6}{:0=6}".format(ans[i][0],ans[i][1]))
