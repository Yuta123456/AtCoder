from collections import deque
import sys
sys.setrecursionlimit(10**7)
t = int(input())
memo = dict()
def calc(n):
    global a,b,c,d
    #print(n)
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return d
    res = d * n
    #何らかの操作を行った後、2で割る
    if n % 2 == 0:
        res = min(res, calc(n//2) + a)
    else:
        res = min(res, calc((n + 1)//2) + a + d, calc((n - 1)//2) + a + d)
    
    if n % 3 == 0:
        res = min(res, calc(n//3) + b)
    else:
        res = min(res, calc((n - (n % 3))//3) + b + d * (n % 3),
         calc((n + (3 - (n % 3)))//3) + b + d * (3 - (n % 3)))

    
    if n % 5 == 0:
        res = min(res, calc(n//5) + c)
    else:
        res = min(res, calc((n - (n % 5))//5) + c + d * (n % 5),
         calc((n + (5 - (n % 5)))//5) + c + d * (5 - (n % 5)))
    memo[n] = res
    #print("n : {} ,  res : {}".format(n,memo[n]))
    return memo[n]

for _ in range(t):
    n, a, b, c, d = map(int, input().split())
    print(calc(n))
    memo = dict()