n, k = map(int, input().split())
ans = 0
for i in range(2,2*n+1):
    if i <= n:
        alpha = i - 1
    else:
        alpha = n - (i - n) + 1
    if (i - k) <= n:
        beta = (i - k - 1)
    else:
        beta =  n - (i - k - n) + 1
    if alpha < 0 or beta < 0:
        continue
    #print("a:{} b:{}".format(alpha, beta))
    ans += alpha * beta
print(ans)