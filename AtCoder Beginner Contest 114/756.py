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
"""
「約数を x 個持つ数の個数」を 
 x の小さい順に求めていく解法。
"""
n = int(input())
dp = [0 for i in range(76)]
dp[1] = 1
