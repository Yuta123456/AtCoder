L = input()
#dp1[k] := k桁目までを確定させ、その時点でA+BがL以下が確定
#dp2[k] := k桁目までを確定させ、その時点でA+BがL以下が確定していない
dp1 = [0 for i in range(len(L))]
dp2 = [0 for i in range(len(L))]
mod = 10**9 + 7
dp1[0] = 1 # A,Bの最上位bitが(0,0)
dp2[0] = 2 # A,Bの最上位bitが(0,1), (1,0)の二通り
#最上位bitを(1,1)にしてしまうと、Lを超えてしまうのでない
for i in range(1,len(L)):
    #dp1の更新から行う
    if L[i] == '1':
        dp1[i] = dp1[i-1] * 3 + dp2[i-1]
        dp2[i] = dp2[i-1] * 2
    else:
        dp1[i] = dp1[i-1] * 3
        dp2[i] = dp2[i-1]
    dp1[i] %= mod
    dp2[i] %= mod
print((dp1[-1] + dp2[-1]) % mod)
