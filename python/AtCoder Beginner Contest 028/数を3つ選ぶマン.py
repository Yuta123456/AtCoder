import itertools
a = list(map(int, input().split()))
ans = []
for i ,j, k in itertools.combinations(range(5), 3):
    ans.append(a[i] + a[j] + a[k])
ans.sort()
print(ans[-3])
