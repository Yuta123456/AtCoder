import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
data = []
inf = 10**10
adjacent_list = [[] for i in range(n+1)]
for i in range(m):
    l,r,d = map(int, input().split())
    adjacent_list[l].append([r,d])
    adjacent_list[r].append([l,-d])
finished = set()
x = [0 for i in range(n+1)]
def dfs(node):
    finished.add(node)
    for nex, dis in adjacent_list[node]:
        if nex not in finished:
            x[nex] = x[node] + dis
            dfs(nex)
        else:
            if x[nex] != x[node] + dis:
                print("No")
                exit()
for i in range(1,n+1):
    if i not in finished:
        dfs(i)
print("Yes")

