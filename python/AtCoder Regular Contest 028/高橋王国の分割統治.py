import sys
sys.setrecursionlimit(10**7)
n = int(input())
tree = [[] for i in range(n)]
for i in range(n-1):
    p = int(input())
    tree[p].append(i+1)
count = [0 for i in range(n)]
def count_children(node):
    if len(tree[node]) == 0:
        count[node] = 0
        return count[node]
    else:
        for i in tree[node]:
            count[node] += 1 + count_children(i)
        return count[node]
count_children(0)
for i in range(n):
    ans = 0
    for j in tree[i]:
        ans = max(ans, count[j] + 1)
    ans = max(ans, n - (1 + count[i]))
    print(ans)
    



