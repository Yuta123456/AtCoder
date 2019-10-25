n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
bl = [0 for i in range(n)]
bl[0] = a[0]
br = [0 for i in range(n)]
br[0] = a[n - 1]
for i in range(1, n):
    bl[i] = max(bl[i - 1],a[i])
a.reverse()
for i in range(1, n):
    br[i] = max(br[i - 1],a[i])
br.reverse()
print(br[1])
for i in range(1, n - 1):
    print(max(bl[i - 1],br[i + 1]))
print(bl[n - 2])
