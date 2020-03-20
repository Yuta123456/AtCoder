n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
d.sort()
t.sort()
index = 0
for i in range(m):
    if index >= n:
        print("NO")
        exit()
    while index < n and t[i] != d[index]:
        index += 1
    if index >= n:
        print("NO")
        exit()
    if t[i] != d[index]:
        print("NO")
    else:
        index += 1
print("YES")