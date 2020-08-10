n, a, b = list(map(int, input().split()))
#min > max n == 0
if a > b or n == 0:
    print(0)
    exit()
#n = 1 and  min != max
if n == 1 and  a != b :
    print(0)
    exit()
print((a + b * (n - 1)) - (a * (n - 1) + b) + 1)