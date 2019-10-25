n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i % n] ^ a[(i + 1) % n] ^ a[(i + 2) % n] != 0:
        print("No")
        exit()
