n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7
def mod_pow(n, k):
    ans = 1
    while k > 0:
        ans = ans * n % mod
        k -= 1
    return ans
if n % 2 == 0:
    a.sort()
    for i in range(n//2):
        if a[2 * i] != a[2 * i + 1] or a[2 * i] != 2 * i + 1:
            print(0)
            exit()
else:
    a.sort()
    if a[0] != 0:
        print(0)
        exit()
    else:
        a = a[1:]
        for i in range(n//2):
            if a[2*i] != a[2 * i + 1] or a[2 * i] != 2*i + 2:
                print(0)
                exit()
print(mod_pow(2, n//2))