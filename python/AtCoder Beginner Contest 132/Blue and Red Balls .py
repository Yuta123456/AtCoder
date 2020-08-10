import numpy as np
import math

n , k = list(map(int, input().split()))
def combi(a,b):
    return  math.factorial(a) // (math.factorial(b) * math.factorial(a-b))
i = 2
mod = 10 ** 9 + 7
for i in range(1, k + 1):
    if n - k + 1 >= i and k - 1 >= i - 1:
        print(int(combi(n - k + 1,i) * combi(k - 1, i - 1) % mod))
    else:
        print(0)
