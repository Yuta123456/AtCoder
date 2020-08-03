n = int(input())
nodes = 0
edges = 0
used = [1 for i in range(n+1)]
if n == 1:
    print(1)
    exit()
for i in range(n-1):
    a, b = map(int, input().split())
    nodes += used[a] * a * (n-a+1) + used[b] * b * (n-b+1)
    used[a] = used[b] = 0
    edges += min(a,b) * (n - max(a,b) + 1)
print(nodes - edges)