import sys
sys.setrecursionlimit(10**9)
k = int(input())
if k == 1:
    print("1 1")
    exit()
k += 1
a,b = 1,0
while k > 0:
    k -= 1
    tmp = a
    a = b + a
    b = tmp
print("{} {}".format(a,b))
