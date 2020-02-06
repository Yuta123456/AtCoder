import copy
n, d, k = map(int, input().split())
data = []
for i in range(d):
    data.append(list(map(int, input().split())))
nationals = []
ans = [d for i in range(k)]
for i in range(k):
    nationals.append(list(map(int, input().split())))
cur_na = copy.deepcopy(nationals)
for i in range(d):
    l,r = data[i]
    for j in range(k):
        #目的地のほうが大きい場合
        if nationals[j][0] < nationals[j][1]:
            if l <= cur_na[j][0] <= r:
                cur_na[j][0] = max(cur_na[j][0], r)
                if cur_na[j][0] >= cur_na[j][1]:
                    ans[j] = min(ans[j], i+1)
        #目的地のほうが小さい場合
        else:
            if l <= cur_na[j][0] <= r:
                cur_na[j][0] = min(l, cur_na[j][0])
                if cur_na[j][0] <= cur_na[j][1]:
                    ans[j] = min(ans[j], i+1)
for i in range(k):
    print(ans[i])