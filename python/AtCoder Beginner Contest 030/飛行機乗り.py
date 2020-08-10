import bisect
n, m  = map(int, input().split())
x,y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_index = 0
b_index = 0
ans = 0
#aにいるときは偶数。bにいるときは奇数
gone = 0
while True:
    if gone % 2 == 0:
        b_index = bisect.bisect_left(b, a[a_index] + x)
        if b_index >= m:
            break
        gone += 1
    else:
        a_index = bisect.bisect_left(a, b[b_index] + y) 
        gone += 1
        ans += 1
        if a_index >= n:
            break
print(ans)