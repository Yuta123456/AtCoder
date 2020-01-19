n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort()
data.reverse()
cur_max = 10**6
pre_2 = 0
pre_1 = 10**6
ans = 0
for i in range(n):
    if pre_1 != data[i][0]:
        if pre_2 != -1:
            cur_max = pre_2
            ans += 1
        if data[i][1] < cur_max:
            pre_2 = data[i][1]
        else:
            pre_2 = -1
    else:
        if  pre_2 < data[i][1] < cur_max:
            pre_2 = data[i][1]
    pre_1 = data[i][0]
    