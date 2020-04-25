import math
length = list(map(int, input().split()))
length.sort()
if length[0] + length[1] >= length[2]:
    print(sum(length)**2 * (math.pi))
else:
    ans = sum(length)**2 * (math.pi)
    l = length[2] - length[1] - length[0]
    ans -= l*l*math.pi
    print(ans)
