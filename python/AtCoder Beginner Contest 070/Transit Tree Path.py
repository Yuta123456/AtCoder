import sys
sys.setrecursionlimit(200000)
n = int(input())
#値の初期化
path = [None]*(n + 1)
adjacent_list = [[] for i in range(n+1)]

for i in range(n - 1):
    a, b, c = list(map(int,input().split()))
    adjacent_list[a].append([b,c])
    adjacent_list[b].append([a,c])
#ノード番号、そこまでの距離,検索済みの要素を受け取る。
def dfs(node_n ,distance,finished):
    #検索済みに追加
    finished.add(node_n)
    #そこまでの距離を代入。値の更新などは特にない（はず）
    path[node_n] = distance
    #対象ノードに対する隣接リストをforで回す
    for i in adjacent_list[node_n]:
        next = i[0]
        if next not in finished:
            #検索済みでなかった場合、そこまでのコストを追加し再帰
            dfs(next, distance + i[1],finished)

q,k = list(map(int, input().split()))
dfs(k, 0, set())
#各クエリへの返答
for i in range(q):
    s, g = list(map(int, input().split()))
    print(path[s] + path[g])