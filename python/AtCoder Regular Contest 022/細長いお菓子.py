n = int(input())
a = list(map(int, input().split()))
kind = set()
index = [-1 for i in range(10**5+1)]
ans = 0
now_l = 0
p = 0
for i in range(n):
    if a[i] in kind:
        pre = index[a[i]]
        now_l = i - pre
        while p != pre + 1:
            if a[p] in kind:
                kind.remove(a[p])
            p += 1
    else:
        now_l += 1
    kind.add(a[i])
    index[a[i]] = i
    ans = max(ans, now_l)
print(ans)