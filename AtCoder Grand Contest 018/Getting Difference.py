from fractions import gcd
#操作の中で値が増えることはないため、max(a) < kだった場合は無理 
n,k = map(int, input().split())
a = list(map(int, input().split()))
gcd_a = a[0]
for i in range(n):
    gcd_a = gcd(gcd_a,a[i])
if k % gcd_a == 0 and k <= max(a):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")