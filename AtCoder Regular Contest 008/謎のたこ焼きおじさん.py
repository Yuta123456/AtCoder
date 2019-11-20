import collections
import math
n,m = list(map(int, input().split()))
name = input()
kit = input()
name_count = collections.Counter(name)
kit_count = collections.Counter(kit)
ans = 0
for i in name_count.keys():
    if i not in kit_count:
        print(-1)
        exit()
    else:
        ans = max(ans, math.ceil(name_count[i]/kit_count[i]))
print(ans)