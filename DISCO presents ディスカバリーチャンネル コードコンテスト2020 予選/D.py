m = int(input())
ans = 0
num = ""
for i in range(m):
    d, c = input().split()
    d = int(d)
    if len(c) > 8:
        num += c[:8]
        c = int(c[8:])
        num += 
    else:
        c = int(c)
    if d == 0:
        ans += c
    else:
        k = str(d) * c
        while len(k) > 1:
            if len(k) > 2:
                k = str(int(k[0]) + int(k[1])) + k[2:]
            else:
                k = str(int(k[0]) + int(k[1]))
            ans += 1
        num += k
while len(num) > 1:
    if len(num) > 2:
        num = str(int(num[0]) + int(num[1])) + num[2:]
    else:
        num = str(int(num[0]) + int(num[1]))
    ans += 1
print(ans)