n, m, k = list(map(int, input().split()))
for i in range(m+1):
    for j in range(n+1):
        if (n * i) + (m * j) - 2 * (i * j) == k:
            print("Yes")
            exit()
print("No")