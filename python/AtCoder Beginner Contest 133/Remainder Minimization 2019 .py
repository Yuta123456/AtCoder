l, r = list(map(int,input().split()))
mod = 2019
min = 2019
for i in range(l, r + 1):
    for j in range(i + 1, r + 1):
        if min > (i * j) % mod:
            min = (i * j) % mod
        if min == 0:
            print(0)
            exit()
print(min)
