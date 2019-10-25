n, k = list(map(int, input().split()))
Gem = list(map(int, input().split()))
gem = []
Max = Gem[0]
r = min(n,k)
for i in range(r + 1):
    gem = []
    for j in range(r - i + 1):
        gem = Gem[0:i]
        gem += Gem[n - j:n]
        dif = k - (i + j)
        for s in range(dif):
            if len(gem) == 0:
                break
            M = gem.index(min(gem))
            if gem[M] < 0:
                del gem[M]
            else:
                break
        if len(gem) == 0:
            Max = max(Max,0)
        elif Max < sum(gem):
            Max = sum(gem)
print(Max)
