import collections
h, w = list(map(int, input().split()))
inf = h * w + 1
sharp = 0
data = []
for i in range(h):
    data.append(list(input()))
    # #の数を数えておく
    sharp += data[i].count('#')

ans = [[inf for i in range(w)] for j in range(h)]
def dfs(row, column, count,data):
    #もし配列の外を参照しているようであれば終了させる
    if(row > w - 1) or (column > h - 1) or ( row < 0 ) or ( column < 0 ):
        return

    if data[column][row] == '#':
        return
    data[column][row] == '#'
    #探索済みなので＃を入れたが、もっと良い方法があるかもしれない
    count += 1
    if row == w - 1 and column == h - 1:
        ans[column][row] = min(count, ans[column][row])
        return
    #その場所がゴールならば終了。ansにそこまでのコストを追加
    ##dataの写しを引数として渡したい。参照渡しか値渡しかを確認
    #+-1ずつ四方向に全探索
    dfs(row + 1, column,     count, data)
    dfs(row,     column + 1, count, data)
    dfs(row - 1, column,     count, data)
    dfs(row,     column - 1, count, data)
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


bfs(0, 0, 0,data)
if ans[-1][-1] == inf:
    print(-1)
    exit()
print(h * w - sharp - ans[-1][-1])
