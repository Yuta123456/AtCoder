q,h,s,d = map(int, input().split())
n = int(input()) * 100
#値の更新をしていく
h = min(h,q*2)
s = min(s,h*2)
d = min(d,s*2)
ans = 0
count = 0
count = n//200
ans += count * d
n -= count*200

count = n//100
ans += count * s
n -= count*100

count = n//50
ans += count * h
n -= count*50

count = n//25
ans += count * q
n -= count*25
print(ans)