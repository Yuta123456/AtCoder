n, a, b, c = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(int(input()))
min = 10**20
def dfs(depth, v):
    if depth >= n:
        if 0 in v and 1 in v and 2 in v:
            calc(v)
    else:
        for i in range(4):
            v[depth] = i
            dfs(depth + 1, v)

def calc(array):
    A = 0
    B = 0
    C = 0
    count = -3
    global min
    for i in range(n):
        if array[i] == 0:
            A += l[i]
            count += 1
        elif array[i] == 1:
            B += l[i]
            count += 1
        elif array[i] == 2:
            C += l[i]
            count += 1
    if min > abs(A - a) + abs(B - b) + abs(C - c) + count * 10 :
        min = abs(A - a) + abs(B - b) + abs(C - c) + count * 10

v = [0 for i in range(n)]
dfs(0,v)
print(min)
