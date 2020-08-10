n, k = map(int, input().split())
a = list(map(int, input().split()))
#dp[i] := 残りi個になったときに先手が勝つかどうか？
dp = [False for i in range(k+1)]
for i in range(n):
    dp[a[i]] = True
#結局dp[k]がTrueなのかFalseなのかを知りたい
for i in range(k+1):
    if dp[i] == False:
        for j in range(n):
            if i + a[j] <= k:
                dp[i+a[j]] = True
if dp[k]:
    print("First")
else:
    print("Second")