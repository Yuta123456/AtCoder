import itertools
n,m,p,q,r = map(int,input().split())
edge = [[] for i in range(n+1)]
for i in range(r):
    x,y,z = map(int, input().split())
    edge[x].append((y,z))
candidate = itertools.combinations(range(1, n+1), p)
ans = 0
for member in candidate:
    mens_point = [0 for i in range(m+1)]
    for girl in member:
        point = 0
        for i,p in edge[girl]:
            mens_point[i] += p
    mens_point.sort(reverse=True)
    ans = max(ans, sum(mens_point[:q]))
print(int(ans))