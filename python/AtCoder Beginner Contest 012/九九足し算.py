n = int(input())
k = 2025 - n
for i in range(1, 10):
    if k % i == 0 and k//i <= 9:
        print("{} x {}".format(i, k//i))