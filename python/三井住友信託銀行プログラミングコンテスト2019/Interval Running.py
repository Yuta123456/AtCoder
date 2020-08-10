t1, t2 = map(int, input().split())
a1,a2 = map(int, input().split())
b1, b2 = map(int, input().split())
if t1 * a1 + t2 * a2 == t1 * b1 + t2 * b2:
    print("infinity")
    exit()
#infの処理
#それ以外の処理
#増える値の設定
inc_ta_1 = t1 * a1
inc_ao_1 = t1 * b1
inc_ta_2 = t2 * a2
inc_ao_2 = t2 * b2
t = 0
a = 0
ans = 0
#さっきの高橋‐青木を計算しておく
pre = 0
i = 0
change = 1
while True:
    if i % 2 == 0:
        t += inc_ta_1
        a += inc_ao_1
    else:
        t += inc_ta_2
        a += inc_ao_2
    #さっきと今の符号が違ったら交点がある
    if pre * (t - a) < 0:
        ans += 1
        change = 1
    else:
        if change == 0:
            print(ans)
            exit()
        change = 0
    pre = t - a
    i += 1
    i %= 2
print(ans)