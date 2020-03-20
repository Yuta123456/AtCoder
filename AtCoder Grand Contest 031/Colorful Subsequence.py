n = int(input())
s = input()
mod = 10**9+7
#文字ごとの累積和を取っておく
acc_char = [0 for i in range(26)]
ans = 0
for i in range(n):
    #今回の数字は使うの確定
    char = s[i]
    plus = 1
    for j in range(len(acc_char)):
        if (ord(char) - ord('a')) != j:
            plus *= acc_char[j] + 1
    ans += plus
    ans %= mod
    acc_char[ord(char) - ord('a')] += 1
print(ans%mod)