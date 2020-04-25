import itertools
n,m = map(int, input().split())
fp = list(map(int, input().split()))
candidate = itertools.combinations([i+1 for i in range(n)], 9)
combo_imformation = []
for i in range(m):
    combo_imformation.append(list(map(int, input().split())))
ans = 0
for member in candidate:
    point = 0
    for i in member:
        point += fp[i-1]
    for combo in combo_imformation:
        set_m = set(member)
        count = 0
        for i in range(combo[1]):
            if combo[i+2] in set_m:
                count += 1
        if count >= 3:
            point += combo[0]
    ans = max(ans, point)
print(ans)


