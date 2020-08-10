import sys
sys.setrecursionlimit(10**5)
n = int(input())
adjacent_list = [[i] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int ,input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
c = list(map(int, input().split()))
c.sort(reverse=True)
k = sorted(adjacent_list,key = lambda x:len(x),reverse=True)
ans = 0
node_num = [-1 for i in range(n+1)]
index = 0
for i in range(n):
    node_num[k[i][0]] = c[i]
#print(node_num)
#現在、出次数が多い順にnodeに数字を振り分けた
finished = set()
def dfs(node):
    global ans
    finished.add(node)
    #print(node)
    for i in adjacent_list[node][1:]:
        #print("node:{} ad:{}".format(node, adjacent_list[node][1:]))
        if i not in finished:
            ans += min(node_num[i], node_num[node])
            dfs(i)
dfs(1)
print(ans)
for i in range(1,n+1):
    print(node_num[i], end=" ")