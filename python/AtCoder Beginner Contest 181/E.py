n, m = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))
h.sort()
import bisect
c = 0
arr = [0 for i in range(n)]
dif = [0 for i in range(n-1)]
odd = [0 for i in range(n)]
even = [0 for i in range(n)]
for i in range(n-1):
    dif[i] = h[i+1] - h[i]
for i in range(n-1):
    odd[i] = odd[i-1]
    even[i] = even[i-1]
    if i % 2 == 0:
        odd[i] = odd[i-1] + dif[i]
    else:
        even[i] = even[i-1] + dif[i]
odd = [0] + odd[:-1]
even = [0] + even[:-1]
ans = 10**18
for i in range(m):
    index = bisect.bisect_right(h, w[i])
    count = 0
    if index % 2 == 0:
        count += abs(h[index] - w[i])
        if index != 0:
            count += odd[index-1]
            count += even[-1] - even[index]
        else:
            count += even[-1]
    else:
        count += abs(h[index-1] - w[i])
        if index != n:
            count += odd[index-1]
            count += even[-1] - even[index]
        else:
            count += odd[-1]
    ans = min(ans, count)
print(ans)