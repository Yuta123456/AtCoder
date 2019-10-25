import math

n, k = map(int, input().split())
a = list(map(int, input().split()))
num = 2 ** (max(int(math.log2(max(a))) + 1, int(math.log2(k + 0.0001)) + 1))
num2 = int(math.log2(num))
for i in range(n):
    a[i] = bin(a[i] + num)[3:]
binary = [[i,0,0] for i in range(num2)]
for i in range(n):
    for j in range(num2):
        if a[i][j] == "0":
            binary[num2 - j - 1][1] += 1
        else:
            binary[num2 - j - 1][2] += 1
binary.sort(reverse = True)
ans = 0
check = 0
for i in range(len(binary)):
    if binary[i][1] > binary[i][2]:
        check += 2 ** binary[i][0]
        if check <= k:
            ans += binary[i][1] * (2 ** binary[i][0])
        else:
            check -= 2 ** binary[i][0]
            ans += binary[i][2] * (2 ** binary[i][0])
    else:
        ans += binary[i][2] * (2 ** binary[i][0])
print(ans)
