n,m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
ans = 0
def check(x, li):
    k = format(x, 'b')
    while len(k) < 3:
        k = '0' + k
    p = []
    for i in k:
        if i == '0':
            p.append(-1)
        else:
            p.append(1)
    tmp = [sum(li[i][j] * p[j] for j in range(3)) for i in range(n)]
    tmp.sort(reverse=True)
    return sum(tmp[:m])

for i in range(8):
    ans = max(ans, check(i, data))
print(ans)