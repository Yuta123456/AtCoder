n, q = map(int,input().split())
imos = [0]*(n+2)
for i in range(q):
    l, r = map(int, input().split())
    imos[l] += 1
    imos[r+1] -= 1
for i in range(n):
    imos[i+1] += imos[i]
for i in range(1,n+1):
    if imos[i] % 2 == 0:
        print("0", end = "")
    else:
        print("1", end="")
print()