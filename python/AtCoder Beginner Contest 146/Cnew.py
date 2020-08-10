import sys
sys.setrecursionlimit(10 ** 9)
n = int(input())
adjacent_list = [[] for i in range(n+1)]
data = []
edgedata = {}
for i in range(n-1):
    a, b = list(map(int, input().split()))
    data.append([a,b])
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
max_node = 0
finished = set()
for i in range(1,n):
    if len(adjacent_list[i]) > len(adjacent_list[max_node]):
        max_node = i
k = len(adjacent_list[max_node])
def dfs(node, num):
    node_list = sorted(adjacent_list[node], key = lambda x:len(adjacent_list[x]))
    color_list = [i for i in range(1,k+1) if i != num]
    c_i = 0
    finished.add(node)
    for i in node_list:
        if i not in finished:
            s = min(node, i)
            t = max(node, i)
            vv = str(s)+str(t)
            edgedata[vv] = color_list[c_i]
            dfs(i, color_list[c_i])
            c_i += 1
dfs(k,-1)
print(k)
for i in data:
    sss = (str(i[0]) + str(i[1]))
    print(edgedata[sss])
#output k

