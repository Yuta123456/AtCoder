n,a,b = map(int, input().split())
if b != 0:
    d = list(map(int, input().split()))
    d.sort()
else:
    d = []
d = d + [n+1]
date_count = len(d) - 1
pre_date = 0
for i in range(len(d)):
    span = d[i] - pre_date
    if span > 0:
        date_count += (span - 1)// a
        pre_date = d[i]
    else:
        pre_date = max(pre_date,d[i])
print(n - date_count)