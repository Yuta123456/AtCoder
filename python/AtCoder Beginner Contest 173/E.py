n , k = map(int, input().split())
a = list(map(int, input().split()))
neg = []
pos = []
mod = 10**9+7
for i in range(n):
    if a[i] > 0:
        pos.append(a[i])
    else:
        neg.append(a[i])
neg.sort()
pos.sort(reverse = True)
if (len(pos) == 0 and k % 2 == 1) or n == k:
    ans = 1
    a.sort(reverse = True)
    for i in range(k):
        ans *= a[i]
        ans %= mod
    print(ans % mod)
else:
    #最大化するとき
    min_num = -1
    good_num = 0
    for i in range(0,k+1,2):
        #i個だけnegから取る。
        if i > len(neg) or k - i > len(pos):
            continue
        m = 0
        if i - 1 >= 0:
            m = abs(neg[i-1])
        if k - i - 1 >= 0:
            m = min(m, pos[k-i-1])
        if m >= min_num:
            min_num = m
            good_num = i
    ans = 1
    for i in range(good_num):
        ans *= neg[i]
        ans %= mod
    for i in range(k - good_num):
        ans *= pos[i]
        ans %= mod
    print(ans % mod)