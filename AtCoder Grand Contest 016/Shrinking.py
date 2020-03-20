from copy import deepcopy as cp
s = input()
c = set(s)
ans = 10**9
for ch in c:
    #全ての文字をiにしよう！
    k = cp(s)
    cand = 0
    while len(set(k)) > 1:
        t = ""
        for i in range(len(k)-1):
            if k[i] == ch or k[i+1] == ch:
                t += ch
            else:
                t += k[i]
        cand += 1
        k = cp(t)
    ans = min(cand, ans)
print(ans)

