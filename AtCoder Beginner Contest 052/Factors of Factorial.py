n = int(input())
mod = 7 + 10 ** 9
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
#エラトステネス
P = primes(n)
primes_count = {}
for i in P:
    primes_count[i] = 0
prime_index = 0
for i in range(2,n+1):
    prime_index = 0
    while i > 1:
        if i % P[prime_index] == 0:
            i = i // P[prime_index]
            primes_count[P[prime_index]] += 1
        else:
            prime_index += 1
ans = 1
for i in primes_count.keys():
    ans *= (primes_count[i] + 1)
print(ans % mod)