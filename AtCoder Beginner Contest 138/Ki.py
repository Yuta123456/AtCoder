import sys
sys.setrecursionlimit(10**7)

n, q = list(map(int, input().split()))
adjacent_list = [[] for i in range(n+1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
tree_value = [0]*(n+1)
for i in range(q):
    p, x = map(int, input().split())
    tree_value[p] += x
searched = set()
def dfs(node, count):
    searched.add(node)
    tree_value[node] += count
    for i in adjacent_list[node]:
        if i not in searched:
            dfs(i, tree_value[node])
dfs(1,0)
for i in range(1,n+1):
    print(tree_value[i])
