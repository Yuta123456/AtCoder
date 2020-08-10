import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
ans = 0
#初めから、どこに挿入されるのかを考えておく
Bcount = [0 for i in range(n+1)]
for i in range(1,n+1):
    Bcount[i] = bisect.bisect_left(a, b[i-1]) + Bcount[i - 1]

for i in range(n):
    index = bisect.bisect_left(b,c[i])

    ans += Bcount[index]
print(ans)
