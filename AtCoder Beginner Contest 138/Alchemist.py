n = int(input())
v = list(map(int, input().split()))
v.sort()
sum = 0
sum = v[0] + v[1]
for i in range(1,n - 1):
    sum += v[i + 1] * (2**i)
print(sum / 2**(n - 1))
