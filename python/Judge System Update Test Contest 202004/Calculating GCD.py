import math
n, q = map(int, input().split())
a = list(map(int, input().split()))
s = list(map(int, input().split()))
d = []
x = a[0]
for i in range(n):
    x = math.gcd(x, a[i])
    d.append(x)
d = d + [1]
def binary_search(left, right,target):
    if right - left <= 1:
        return right
    middle = (right + left)//2
    if is_can(middle,target):
        return binary_search(middle, right,target)
    else:
        return binary_search(left, middle,target)
def is_can(middle,target):
    if math.gcd(d[middle],target) == 1:
        return False
    else:
        return True
for i in range(q):
    d_0 = math.gcd(s[i], d[0])
    d_1 = math.gcd(s[i], d[n-1])
    if d_0 == 1:
        print(1)
    elif d_1 != 1:
        print(d_1)
    else:
        print(binary_search(0,n+1,s[i])+1)

