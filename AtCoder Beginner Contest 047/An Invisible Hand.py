n, t = list(map(int, input().split()))
a = list(map(int, input().split()))
dif_list = [0] * n
max_list = [0 for i  in range(n)]
a.reverse()
max_list[0] = a[0]
for i in range(1,n):
    max_list[i] = max(max_list[i-1], a[i])
max_list.reverse()
a.reverse()
for i in range(0,n):
    dif_list[i] = max_list[i] - a[i]

k = max(dif_list)
count = 0
for i in range(n):
    if k == dif_list[i]:
        count += 1
print(count)