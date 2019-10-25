import math
N, K = list(map(int, input().split()))

def combo(n, k):
    x = math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
    return x

for i in range(1,K+1):
    if N-K+1 < i or K-1 < i-1:
        print(0)
    else:
        k = combo(N-K+1,i) * combo(K-1,i-1)
        ans = k%(10**9+7)
        print("%d" %(ans))
