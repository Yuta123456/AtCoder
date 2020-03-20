n = input()
dp1 = [0 for i in range(len(n))]
dp2 = [0 for i in range(len(n))]
# dp1[i] := i桁目まで決めて、nより小さいことが確定している数字の1を書く回数
# dp2[i] := i桁目まで決めた後、nより小さいことが確定していない数字の1を書く回数
if n[0] != '1':
    dp1[0] = 1
else:
    dp2[0] = 1
for i in range(1,len(n)):
    k = int(n[i])
    #好きな数字を選べるので、*10. 
    dp1[i] += dp1[i-1] * 10 + int(n[i-1])
    #同じ数字を選んだ場合
    dp2[i] += dp2[i-1]
    if k > 0:
        #数字の選び方によってdp2がdp1に落ちる
        dp1[i] += dp2[i] * (k + 1)
        if k == 1:
            dp2[i] += 1
        else:
            dp1[i] += 1
print(dp1)
print(dp2)
print(dp2[-1] + dp1[-1])