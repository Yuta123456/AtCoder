import sys
sys.setrecursionlimit(10**7)
n,m = map(int, input().split())
adjacent_list = [[] for i in range(n+1+m+1)]
for i in range(1,n+1):
    for j in list(map(int, input().split()))[1:]:
        adjacent_list[i].append(j+n)
        adjacent_list[j+n].append(i)
finished = set()
def dfs(node):
    finished.add(node)
    for i in adjacent_list[node]:
        if i not in finished:
            dfs(i)
dfs(1)
flag = True
for i in range(1,n+1):
    if i not in finished:
        flag = False
if flag:
    print("YES")
else:
    print("NO")