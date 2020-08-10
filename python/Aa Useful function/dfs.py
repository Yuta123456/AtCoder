#重み有り。
def dfs(node,cost):
    finished.add(node)
    for i in adjacent_list[node]:
        if dist[node] + i[1] < dist[i[0]]:
            dist[i[0]] = dist[node] + i[1]
            dfs(i[0],i[1])