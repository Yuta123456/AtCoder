from collections import defaultdict
from copy import deepcopy as cp
n = int(input())
s_1 = list(input())
s_2 = list(input())
d = defaultdict(list)
#グラフを作る
for i in range(n):
    d[s_1[i]].append(s_2[i])
    d[s_2[i]].append(s_1[i])
ans = cp(s_1)
def dfs(node):
    finished.add(node)
    for i in d[node]:
        if i not in finished:
            dfs(i)
    

for i in range(n):
    finished = set()
    dfs(ans[i])
    for j in finished:
        ans[i] = min(ans[i], j)
res = 1
finished = set()
for i in range(n):
    if ans[i].isdigit() or ans[i] in finished:
        continue
    else:
        if i == 0:
            res *= 9
        else:
            res *= 10
        finished.add(ans[i])
print(res)