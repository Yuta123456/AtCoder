import sys
sys.setrecursionlimit(10 ** 7)
n = int(input())
#隣接リスト
adjacent_list = [[] for i in range(n+1)]
#入力されたデータを保存しておくやつ
data = [None] * (n - 1)
#最終的に色を入れておくやつ。
#edgedata[(1,2)] => 1->2の辺の色を入れておく
edgedata = {}
for i in range(n-1):
    a, b = list(map(int, input().split()))
    data[i] = [a, b]
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)
#つながってるノードが一番多いやつを保存しておく
max_node = 0
#探索が終わったやつを入れる
finished = set()
for i in range(1,n):
    if len(adjacent_list[i]) > len(adjacent_list[max_node]):
        max_node = i
#kには色の種類を入れる
k = len(adjacent_list[max_node])
#print("k => {}".format(k))
def dfs(node, num):
    #隣接リストの中身を、つながってるノード順にソート
    node_list = sorted(adjacent_list[node], key = lambda x:len(adjacent_list[x]))
    #さっきつかったいろは使わないようにする
    color_list = [i for i in range(1,len(node_list) + 2) if i != num]
    c_i = 0
    finished.add(node)
    for i in node_list:
        #まだ見てなかったら、dfsを掛ける
        if i not in finished:
            #小さいほうから大きいほうに文字を並べ、ハッシュに値を保存
            #print("{}".format(color_list))
            #print("c_i =>{}  node =>{}".format(c_i,node))
            edgedata[(min(node, i), max(node, i))] = color_list[c_i]
            #color_list[c_i]は使ったので、使った色として引数で渡す。
            dfs(i, color_list[c_i])
            #この色は使ったから、一個ずらす
            c_i += 1
#一番のノードを根とし、dfsをかける
dfs(k,-1)
print(k)
for i in data:
    print(edgedata[tuple(i)])
#output k
