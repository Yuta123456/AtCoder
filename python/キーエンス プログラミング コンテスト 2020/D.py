from collections import deque
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
odd = []
even = []

for i in range(n):
    if i % 2 == 0:
        even.append(a[i])
        odd.append(b[i])
    else:
        even.append(b[i])
        odd.append(a[i])
#odd, evenの二部グラフで、自身に辺を通さない
#a[i] <=  b[j]の時辺を通す 
graph = [[] for i in range(n*2)]
for i in range(n):
    for j in range(n, n*2):
        if i != j % n and even[i] <= odd[j%n]:
            graph[i].append(j)

for i in range(n,n*2):
    for j in range(n):
        if  j != i % n and odd[i % n] <= even[j]:
            graph[i].append(j)
#グラフで一筆書きをする。パスがnになったら終わり。その順番を実現するために考える
def clear_maze(start):
    que = deque()
    que.append([start, set([start]), [start]])
    while que:
        node, f, p = que.popleft()
        if len(p) == n:
            check(p)
        else:
            for i in graph[node]:
                if i % n not in f:
                    que.append([i, f|set([i%n]), p + [i]])

def check(path):
    #この順番に並ぶための最小
    #print(path)
    array = [i % n for i in path]
    cand = 0
    global ans
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if array[j] < array[j-1]:
                cand += 1
    ans = min(cand, ans)
inf = 18**2
ans = inf
for i in range(n):
    #iから始める迷路を解く
    clear_maze(i)
if ans == inf:
    print(-1)
else:
    print(ans)
