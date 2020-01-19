def power_(n, p, mod):
    global count
    count += 1
    if p == 1:
        return n
    if p % 2 == 0:
        return (power_(n, p//2, mod) ** 2) % mod
    else:
        return n * (power_(n, p//2, mod) ** 2) % mod
count = 0
print (power_(2,10**9,1000))
print(count)