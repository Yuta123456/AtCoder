s = input()
n = len(s)
num = 10
s = int(s)
ans = 0
for i in range(n):
    p = s//num
    q = (s%num) + 1
    ans += p*(num//10)
    if (num//10)*2 <= q:
        ans += (num//10)
    else:
        ans += max(q - (num//10),0)
    num *= 10
print(ans)