n, m, q = map(int, input().split())
memo  = [[0 for i in range(n+1)] for j in range(n+1)]
ans = [[0 for i in range(n+1)]for j in range(n+1)]
for i in range(m):
    l, r = map(int, input().split())
    memo[l][r] += 1
for i in range(1, n+1):
    for j in range(1, n+1):
        memo[i][j] += memo[i][j - 1]
for i in range(1, n+1):
    for j in range(1, n+1):
        memo[i][j] += memo[i - 1][j]
for i in range(q):
    l, r = map(int, input().split())
    print(memo[r][r] + memo[l-1][l-1] - memo[r][l - 1] - memo[l - 1][r])