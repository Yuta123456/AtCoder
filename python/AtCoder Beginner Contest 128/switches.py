n, m = list(map(int, input().split()))
light = []
for i in range(m):
    k = list(map(int, input().split()))
    aaaaa = [0 for i in range(n)]
    for i in range(k[0]):
        aaaaa[k[i+1] - 1] = 1
    aaaaa = int("".join(map(str, aaaaa)), 2)
    light.append(aaaaa)
p = list(map(int, input().split()))
ans = 0
for i in range(2**n):
    flag = 1
    for j in range(len(light)):
        #print("i{}, j{} light[j] {}".format(i, j, light[j]))
        k = i & light[j]
        if list(bin(k)).count("1") % 2 != p[j]:
            flag = 0
    if flag:
        ans += 1
print(ans)




