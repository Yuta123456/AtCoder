n = int(input())
a = list(map(int, input().split()))
node = [0 for i in range(n+1)]
if n == 0:
    if a[0] != 1:
        print(-1)
        exit()
    else:
        print(1)
        exit()
if a[0] != 0:
    print(-1)
    exit()
node[0] = 1
count = 1
for i in range(1,n+1):
    count = min(count * 2, 10**18)
    if a[i] > count:
        print(-1)
        exit()
    node[i] = node[i-1] - a[i-1]
    node[i] *= 2
if node[-1] < a[-1]:
    print(-1)
    exit()
node[-1] = a[-1]
for i in range(n-1, -1, -1):
    if a[i] > node[i]:
        print(-1)
        exit()
    node[i] = min(node[i], node[i+1] + a[i])
print(sum(node))
