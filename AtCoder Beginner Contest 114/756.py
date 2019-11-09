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
n = int(input())
prime_list = primes(n)
factor = {}
for i in prime_list:
    factor[i] = 0
for i in range(2,n+1):
    num_copy = i
    #prime_listのための添え字
    j = 1
    while num_copy != 1:
        if num_copy % prime_list[j] == 0:
            num_copy /= prime_list[j]
            prime_list[j] += 1
        else:
            j += 1
        


