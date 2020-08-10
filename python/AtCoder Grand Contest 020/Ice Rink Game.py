k = int(input())
a = list(map(int, input().split()))
#そのラウンドで落ちるマックスはa[i]-1人、残る人数は最小でa[i]
#a[i-1] <= 2 でなくてはいけない。
#そのラウンドが終わるごとに人数がa[i]の倍数になっていると考えると分かりやすい
#最大を考える場合は、そのラウンドで毎回毎回max人数落ちてると考えればいい
#最小を考える場合は、そのラウンドで毎回毎回min人数落ちていると考える

if a[-1] > 2:
    print(-1)
    exit()
ans_min = 2
ans_max = 2
a.reverse()
for i in range(k):
    if ans_max % a[i] != a[i] - 1:
        ans_max += (a[i] - 1) - (ans_max % a[i])
    if ans_min % a[i] != 0:
        ans_min += a[i] - ans_min % a[i]
a.reverse()
sim_max = ans_max
sim_min = ans_min
for i in range(k):
    sim_max = sim_max - sim_max % a[i]
    sim_min = sim_min - sim_min % a[i]
if sim_max == sim_min == 2:
    print("{} {}".format(ans_min, ans_max))
else:
    print(-1)