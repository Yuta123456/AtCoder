n = int(input())
a = list(map(int, input().split()))
xor = 0
for i in range(n):
    xor ^= a[i]
for i in range(n):
    print(xor ^ a[i],end = ' ')