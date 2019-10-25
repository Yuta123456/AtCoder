num, yen = map(int ,input().split())
yen /= 1000
for i in range(num + 1):
    for j in range(num + 1 -i):
        k = num - i - j
        if 10 * k + 5 * j + i * 1 == yen:
            print(k,j,i)
            exit()
print(-1, -1, -1)
