n = int(input())
primes = [0 for i in range(n+1)]
for i in range(2,n+1):
    cur = i
    for j in range(2,i+1):
        while cur % j == 0:
            cur = cur // j
            primes[j] += 1
def num(m):
    res = 0
    for i in primes:
        if i >= m-1:
            res += 1
    return res
print(num(75) + (num(5) - 1) * num(5) * (num(3) - 2) // 2
 + num(15) * (num(5) - 1) + num(25) * (num(3) - 1) )
