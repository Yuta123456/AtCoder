import itertools
n, k = map(int, input().split())
acc = list(itertools.accumulate(range(1001)))
p = list(map(int, input().split()))
for i in range(n):
    temp = p[i]
    p[i] = acc[p[i]]
    p[i] /= temp
ans = 0
p = [0] + p
acc_2 = list(itertools.accumulate(p))
for i in range(n-k+1):
    ans = max(ans, acc_2[i+k] - acc_2[i])
print(ans)


