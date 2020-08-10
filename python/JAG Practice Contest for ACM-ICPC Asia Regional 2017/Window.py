n,h,w = map(int, input().split())
x = list(map(int, input().split()))
inner = [0 for i in range(w*n)]
outer = [0 for i in range(w*n)]
inn = 1
for i in range(w*n):
    if i % w == 0:
        inn *= -1
    if inn == 1:
        outer[i] = 1
    else:
        inner[i] = 1
count = 1
flag = False
for i in range(w*n):
    if outer[i] == 1:
        outer[i-x[count]] = 1
        if x[count] != 0:
            outer[i] = 0
        flag = True
    else:
        if flag:
            count += 2
            flag = False
count = n-2
flag = False
inner.reverse()
for i in range(w*n):
    if inner[i] == 1:
        inner[i-x[count]] = 1
        if x[count] != 0:
            inner[i] = 0
        flag = True
    else:
        if flag:
            count -= 2
            flag = False
inner.reverse()
ans = 0
for i in range(w*n):
    if inner[i] == 0 and outer[i] == 0:
        ans += 1
print(ans * h)