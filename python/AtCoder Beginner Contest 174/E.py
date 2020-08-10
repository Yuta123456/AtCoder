import math
import sys
sys.setrecursionlimit(10**8)
n, k = map(int, input().split())
a = list(map(int, input().split()))
def binary_search(left, right):
    if right - left <= 0.01:
        return right
    middle = (right + left) / 2
    if is_can(middle):
        return binary_search(left, middle)
    else:
        return binary_search(middle, right)
def is_can(target):
    count = 0
    for i in range(n):
        if a[i] > target:
            count += a[i] // target
    return count <= k
p = binary_search(0, 10**10)
if int(p) != 0 and is_can(int(p)) :
    print(int(p))
else:
    print(int(p) + 1)
