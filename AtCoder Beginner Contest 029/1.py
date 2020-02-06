n = input()
ans = 0
#dp[i] := '9'*iまでの1の数
#ex) dp[3] => 999まで1の数 
dp = [0 for i in range(len(n))]
dp[0] = 0
for i in range(len(n)-1):
    dp[i+1] = dp[i] + 9 * dp[i] + 1
print(dp)
for i in range(len(n)):
    ans += (int(n[i]) + 1) * dp[len(n) - i - 1] + 10 ** (len(n) - i - 1) 
print(ans)


