n, h = list(map(int, input().split()))
a = [0 for i in range(n)]
b = [0 for i in range(n)]
for i in range(n):
    a[i], b[i] = list(map(int, input().split()))
f = max(a)
b.sort()
for i in range(n):
    if b[i] <= f:
        b[i] = 0
    else:
        break

total = 0
count = 0
b.reverse()
for i in range(n):
    if b[i] == 0:
        break
    total += b[i]
    count += 1
    if total >= h:
        print(count)
        exit()
if (h - total) % f == 0:
    count += (h - total) // f
else:
    count += (h - total) // f
    count += 1
print(count)
