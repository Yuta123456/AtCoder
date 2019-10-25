def ceil(x):
    k = x % 10
    if k == 0:
        return x
    else:
        return x + (10 - k)
d = []
for i in range(5):
    d.append(int(input()))
d_min = []
min = 124
sum = 0
index = -1
for i in range(5):
    d_min.append((d[i]) % 10)
for i in range(5):
    if d_min[i] != 0:
        if min > d_min[i]:
            min = d_min[i]
            index = i
if index == -1:
    index = 0
for i in range(5):
    if i != index:
        sum = sum + ceil(d[i])
sum += d[index]
print(sum)
