n, k = list(map(int, input().split()))
x = list(map(int, input().split()))
i = 0
mi = x[-1] - x[0] + min(abs(x[-1]),abs(x[0]))
if n == 1:
    print(abs(x[0]))
    exit()
while i <= n - k:
    if mi >= ( x[i + k - 1] - x[i]) + min(abs(x[i + k - 1]),abs(x[i])):
        mi = (x[i + k - 1] - x[i]) + min(abs(x[i + k - 1]),abs(x[i]))
    i += 1
print(mi)
