first, last = input().split()
n = int(input())
strings = [first, last]
for i in range(n):
    strings.append(input())
strings = list(set(strings))
node_count = len(strings)
adjacent_list = [[] for i in range(node_count)]

for src in range(node_count):
    for tar in range(src+1, node_count):
        src_string = strings[src]
        tar_string = strings[tar]
        dif_count = 0
        for ch_i in range(len(src_string)):
            if src_string[ch_i] != tar_string[ch_i]:
                dif_count += 1
        if dif_count == 1:
            adjacent_list[src].append(tar)
            adjacent_list[tar].append(src)
from heapq import heappush, heappop
def dijkstra(start,graph):
    INF = 10 ** 5
    dist = [INF] * (node_count+1)
    dist[start] = 0
    q = [(0,start)]
    while q:
        d,v = heappop(q)
        if dist[v] < d:
            continue
        for w in graph[v]:
            d1 = d + 1
            if dist[w] > d1:
                dist[w] = d1
                heappush(q, (d1,w))
    return dist
start_index = strings.index(first)
end_index = strings.index(last)
s_dist_list = dijkstra(start_index, adjacent_list)
e_dist_list = dijkstra(end_index, adjacent_list)
str_to_index = dict()
for i in range(node_count):
    str_to_index[strings[i]] = i
if first == last : 
    print(0)
    print(first)
    print(last)
elif s_dist_list[end_index] == 10**5 : 
    print(-1)
else:
    print(s_dist_list[end_index] - 1)
    print(first)
    now_steps = s_dist_list[end_index] - 1
    now_string_num = start_index
    for i in range(s_dist_list[end_index] - 1):
        for index in adjacent_list[now_string_num]:
            if e_dist_list[index] == now_steps:
                now_steps -= 1
                now_string_num = index
                print(strings[index])
                break
    print(last)
