n = int(input())
a = list(map(int, input().split()))
ans = [0 for i in range(n)]
def sum_array(ans, k):
    sum = 0
    for i in range(n):
        if (i + 1) % (k + 1) == 0:
            sum += ans[i]
    return sum
for i in range(n):
    if sum_array(ans, n - i - 1) % 2 != a[n - i - 1]:
        ans[n - i - 1]  += 1
print(sum(ans))
for i in range(n):
    print("{} ".format(ans[i]), end = '')
