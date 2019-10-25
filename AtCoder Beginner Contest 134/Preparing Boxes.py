n = int(input())
a = list(map(int, input().split()))
Ans = [0 for i in range(n)]
for i in range(1,n + 1)[::-1]:
    count = 0
    mul = 1
    k = i
    while k * mul <= n:
        count += Ans[k * mul - 1]
        mul += 1
    if count % 2 != a[i - 1]:
        Ans[i - 1] = 1
print(sum(Ans))
for i in range(1, n + 1):
    if Ans[i - 1] == 1:
        print("{} ".format(i), end = " ")
