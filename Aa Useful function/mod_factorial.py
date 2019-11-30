def mod_factorial(n):
    ans = 1
    while n >= 2:
        ans  = (ans * n) % mod
        n -= 1
    return ans