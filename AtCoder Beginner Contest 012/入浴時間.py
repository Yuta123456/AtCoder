import math
n = int(input())
h = math.floor(n/3600)
n -= h*3600
m = math.floor(n/60)
n -= m*60
s = n
if h >= 24:
    print("23:59:59")
else:
    print("{:02d}:{:02d}:{:02d}".format(h,m,s))