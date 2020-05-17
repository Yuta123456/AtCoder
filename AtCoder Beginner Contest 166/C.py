n,m = map(int, input().split())
h = list(map(int, input().split()))
adjacent_list = [[] for i in range(n+1)]
def check(node):
    now = h[node-1]
    for i in adjacent_list[node]:
        if now <= h[i-1]:
            return False
    return True
for i in range(m):
    a,b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
ans = 0
for i in range(1,n+1):
    if check(i):
        ans += 1
print(ans)