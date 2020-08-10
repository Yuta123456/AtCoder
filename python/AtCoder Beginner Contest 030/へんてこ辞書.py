import math
n, a = map(int, input().split())
k = int(input())
b = list(map(int, input().split()))
adjacent_list = [-1 for i in range(n+1)]
for i in range(1, n+1):
    adjacent_list[i] = b[i-1]
route = []
finished = set()
def dfs(node):
    if node in finished:
        route.append(node)
        return
    else:
        finished.add(node)
    route.append(node)    
    dfs(adjacent_list[node])
dfs(a)
index = route.index(route[-1])
if k < index:
    print(route[k])
    exit()
k -= index
k %= len(route) - index - 1
print(route[index:-1][k])

