import itertools
n = int(input())
a = list(map(int, input().split()))
count = []
cc = 1
for i in range(1,n):
    if a[i-1] >= a[i]:
        count.append(cc)
        cc = 0
    cc += 1
count.append(cc)
ans = 0
pppp = max(count)
pppp = list(itertools.accumulate(range(pppp+1)))
for i in count:
    ans += pppp[i]
print(ans)