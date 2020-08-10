import math
n, p = map(int ,input().split())
#引数　n, 返り値nまでの素数をリストで返す
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    #根号
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
ff = primes(int(math.sqrt(p) + 1))
ans = 1
factorized = dict(zip(ff, [0 for i in range(len(ff))]))
if n == 1:
    print(p)
    exit()
for i in factorized.keys():
    while p % i == 0:
        p /= i
        factorized[i] += 1
    
for i in factorized.keys():
    if factorized[i] >= n :
        ans *= i**(factorized[i] // n)
print(ans)
