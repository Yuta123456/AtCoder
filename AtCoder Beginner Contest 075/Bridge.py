n,m = map(int, input().split())
data = []
for i in range(m):
    data.append(list(map(int, input().split())))

not_bridge = 0
def dfs(node, finished):
    finished.add(node)
    global not_bridge
    if len(finished) == n:
        not_bridge += 1
    else:
        for i in adjacent_list[node]:
            if i not in finished:
                dfs(i, finished)
    
#iが省く要素
for i in range(m):
    adjacent_list = [[]for i in range(n+1)]
    finished = set()
    for j in range(m):
        if i != j:
            a, b = data[j]
            adjacent_list[a].append(b)
            adjacent_list[b].append(a)
    dfs(1, finished)
print(m - not_bridge)
