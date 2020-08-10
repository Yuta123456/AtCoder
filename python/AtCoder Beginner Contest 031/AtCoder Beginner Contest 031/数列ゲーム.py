n = int(input())
a = list(map(int, input().split()))
cand = []
#t_i : 高橋君の丸つけるやつ　a_iは青木君
for t_i in range(n):
    ans = -1 * 10**5
    c = 0
    for a_i in range(n):
        if a_i == t_i:
            continue
        min_i = min(t_i, a_i)
        max_i = max(t_i, a_i)
        k = a[min_i:max_i+1]
        aoki = 0
        takahashi = 0
        for j in range(len(k)):
            if j % 2 == 0:
                takahashi += k[j]
            else:
                aoki += k[j]
        if ans < aoki:
            ans = aoki
            c = takahashi
    cand.append(c)
print(max(cand))

        