from scipy.sparse.csgraph import floyd_warshall

#input
h, w = list(map(int, input().split()))

c = [0 for i in range(10)]
for i in range(10):
    c[i] = list(map(int, input().split()))

wall = []

for i in range(h):
    wall.append(list(map(int, input().split())))

#solve
#1へのコスト
costone = [(10**3) + 1 for i in range(11)]
#-1, 1はコストがかからないため０で初期化
costone[1] = 0
#-1の処理
costone[10] = 0
#ワーシャルフロイド法を使う
#iは出発、jは経由,
c = floyd_warshall(c)
##for i in range(10):
##    for j in range(10):
##        for k in range(10):
##            c[i][k] = min(c[i][k], c[i][j] + c[j][k])
#costoneを更新
for i in range(10):
    costone[i] = min(costone[i], c[i][1])
sum = 0


for i in range(h):
    for j in range(w):
        sum += costone[wall[i][j]]
print(int(sum))
