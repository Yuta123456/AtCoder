N, M = map(int, input().split())
A = list(map(int, input().split()))
table = [0,2,5,5,4,5,6,3,7,6]
A.sort(reverse=True)
inf = (-1) * 10**5
#dp[i] := ちょうどi本のマッチを使って作る整数の、最大桁数
dp = [inf for i in range(N+1)]
dp[0] = 0
for i in range(N+1):
    for j in range(len(A)):
        if i + table[A[j]] > N:
            continue
        if dp[i + table[A[j]]] < dp[i] + 1:
            dp[i + table[A[j]]] = dp[i] + 1
#こうすることで、答えの桁数が分る.
#あとは実現する経路復元のようなものを行う
ans = ""
cur_cost = N
#各桁について一つずつ答えを決めていく
for _ in range(dp[N]):
    #大きい数字から最上位に決めていきたいので、大きい数字から考える
    for j in range(len(A)):
        if cur_cost - table[A[j]] < 0:
            continue
        if dp[cur_cost - table[A[j]]] == dp[cur_cost] - 1:
            ans += str(A[j])
            cur_cost -= table[A[j]]
            break
print(ans)

