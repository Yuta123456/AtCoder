n = int(input())
cand = 0
memo = dict()
ans = 0
for i in range(1, n+1):
    s = str(i)[0]
    f = str(i)[-1]
    if s+f in memo:
        ans += memo[s+f]
    else:
        count = 0
        for j in range(1,n+1):
            q = str(j)[0]
            r = str(j)[-1]
            if q == f and r == s:
                count += 1
        ans += count
        memo[s+f] = count
print(ans)

