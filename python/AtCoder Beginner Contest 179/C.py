from collections import defaultdict
n = int(input())
ans = 0
divide_minimam_prime = [i for i in range(n + 1)]
is_prime = [True for i in range(n + 1)]
is_prime[0] = False
is_prime[1] = False
for div in range(2,int(n**0.5) + 1):
    if is_prime[div]:
        # divが素数だった場合
        k = div
        divide_minimam_prime[k] = k
        k += div
        while k <= n:
            is_prime[k] = False
            if divide_minimam_prime[k] == k:
                divide_minimam_prime[k] = div
            k += div
for i in range(1,n):
    k = i
    use_divnum = defaultdict(int)
    while k != 1:
        div = divide_minimam_prime[k]
        while k % div == 0 and k > 1:
            k = k // div
            use_divnum[div] += 1
    count = 1

    for j in use_divnum.values():
        count *= j + 1
    ans += count
print(ans)