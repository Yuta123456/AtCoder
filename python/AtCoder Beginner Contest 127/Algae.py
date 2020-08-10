r, D, x = list(map(int, input().split()))
count = 0
while count < 10:
    count += 1
    x = r * x - D
    print(x)
