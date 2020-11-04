import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
edge = [list(map(int, input().split())) for i in range(m)]
adjacent_list = [[] for i in range(n+1)]
for i in range(m):
    s, t = edge[i]
    adjacent_list[s].append(t)
    adjacent_list[t].append(s)
def dfs(node):
    finished.add(node)
    for i in adjacent_list[node]:
        if i not in finished:
            dfs(i)
searched = set()
finished = set()
for i in range(1, n+1):
    if i in searched:
        continue
    finished = set()
    dfs(i)
    a_sum = 0
    b_sum = 0
    for node in list(finished):
        a_sum += a[node-1]
        b_sum += b[node-1]
        searched.add(node)
    if a_sum != b_sum:
        print("No")
        exit()
if sum(a) == sum(b):
    print("Yes")
else:
    print("No")