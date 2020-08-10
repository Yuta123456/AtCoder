import sys
from queue import *
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
used = [0 for i in range(n+1)]
que = Queue()
que.put(1)
while que.qsize() != 0:
    m = que.get()
    used[m] = 1
    for i in adjacent_list[m]:
        if not used[i]:
            tree_value[i] += tree_value[m]
for i in range(1,n+1):
    print("{} ".format(tree_value[i]), end = "")
