n = int(input())
a = list(map(int, input().split()))
a.sort()
color = set()
free = 0
for i in range(n):
    if a[i] < 3200:
        color.add(a[i]//400)
    else:
        free += 1
print("{} {}".format(max(1, len(color)), free + len(color)))