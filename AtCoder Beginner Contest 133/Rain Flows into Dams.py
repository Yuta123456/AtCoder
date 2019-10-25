import numpy as np

n = int(input())
a = list(map(int, input().split()))
s = 0
x = [-1 for i in range(n)]
for i in range(1,n):
    if i % 2 == 1:
        s += a[i]
x[0] = sum(a) - s * 2
for i in range(1, n):
    x[i] = a[i - 1] * 2 - x[i - 1]
for i in x:
    print(i,end = "")
    print(" ", end = "")
