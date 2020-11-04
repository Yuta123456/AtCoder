n = int(input())
a = list(map(int, input().split()))
slime_acc = [0 for i in range(n)]
slime_acc[0] = a[0]
for i in range(1,n):
    slime_acc[i] += slime_acc[i-1] + a[i]
slime_acc = [0] + slime_acc
dp = [[-1 for i in range(n)] for j in range(n)]
# dp[l][r] := 区間l,rが合体しているスライムを分解するのに必要なコスト
for i in range(n):
    dp[i][i] = 0
def culc(l, r):
    #print("{} {}".format(l, r))
    if dp[l][r] != -1:
        return dp[l][r]
    c = 10**10
    for i in range(l+1, r):
        # print("l:{} r:{} sum:{}".format(l, r, slime_acc[r+1] - slime_acc[l]))
        c = min(c, culc(l, i) + culc(i+1, r) + slime_acc[r+1] - slime_acc[l])
    dp[l][r] = c
    return dp[l][r]

print(culc(0, n-1))
