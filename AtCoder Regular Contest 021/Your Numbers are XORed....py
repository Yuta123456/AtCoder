l = int(input())
b = []
for i in range(l):
    b.append(int(input()))
xor = 0
for i in range(l):
    xor ^= b[i]
if xor != 0:
    print(-1)
    exit()
ans = 0
for i in range(l):
    print(ans)
    ans = b[i] ^ ans
