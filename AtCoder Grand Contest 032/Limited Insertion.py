n = int(input())
b = list(map(int, input().split()))
b.sort()
b.reverse()
for i in range(n):
    if b[i] > n - i:
        print("-1")
        exit()
b.reverse()
for i in range(n):
    print(b[i])
