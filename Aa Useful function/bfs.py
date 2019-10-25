def bfs(row, column, count,data):
    becter = [-1,1]
    queue = collections.deque()
    queue.append([column, row,count])
    while len(queue) != 0:
        v = queue.popleft()
        if v[0] < 0 or v[1] < 0 or v[0] >= h or v[1] >= w:
            continue
        if data[v[0]][v[1]] != '#':

            data[v[0]][v[1]] = '#'
            v[2] += 1
            ans[v[0]][v[1]] = min(ans[v[0]][v[1]], v[2])
            queue.append([v[0] + 1, v[1],v[2]])
            queue.append([v[0], v[1] + 1,v[2]])
            queue.append([v[0] - 1, v[1],v[2]])
            queue.append([v[0], v[1] - 1,v[2]])
