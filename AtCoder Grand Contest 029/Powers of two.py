from collections import Counter
n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
a.sort(reverse=True)
ans = 0
for num in a:
    if count[num] == 0:
        continue
    else:
        #numより大きい2のべき乗の数
        p = 2 ** num.bit_length()
        if p - num == num:
            if count[p - num] > 1:
                sub = count[num] // 2
                ans += sub
                count[num] -= sub * 2
        else:
            if count[p - num] > 0:
                sub = min(count[p - num], count[num])
                ans += sub
                count[p-num] -= sub
                count[num] -= sub
print(ans)
