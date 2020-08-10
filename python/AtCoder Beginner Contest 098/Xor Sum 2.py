n = int(input())
a = list(map(int, input().split()))
bit_acc = [[0 for i in range(21)] for j in range(n+1)]
for i in range(1,n+1):
    k = format(a[i-1], '021b')
    for j in range(len(k)):
        if k[j] == "1":
            bit_acc[i][j] = bit_acc[i-1][j] + 1
        else:
            bit_acc[i][j] = bit_acc[i-1][j]
right = 1
left = 0
ans = 0
while left <= n:
    flag = True
    for j in range(21):
        if bit_acc[right][j] - bit_acc[left][j] >= 2:
            #print("l {}, r {}".format(left, right))
            ans += right - 1 - left
            left += 1
            flag = False
            break
    if flag:
        if right < n:
            right += 1
        else:
            #print("l {}, r {}".format(left, right))
            ans += right - left
            left += 1
print(ans)
