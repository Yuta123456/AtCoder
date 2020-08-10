import bisect
n,m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()

data = [None] * m
for i in range(m):
    data[i] = list(map(int, input().split()))
data.sort(key = lambda x : x[1])
data.reverse()


ans = 0
count = 0
pre_index = 0
#print(data)
#print(a)
#data[][1] = value, data[][0] = card_num
for i in range(m):
    insert_index = bisect.bisect_left(a, data[i][1])
    count = min(data[i][0], insert_index - pre_index)
    for j in range(pre_index, pre_index + count):
        if j >= n:
            break
        a[j] = 0
    ans += count * data[i][1]
    pre_index = pre_index + count
print(ans + sum(a))
