n = int(input())
ans = 0
c_1 = 0
c_2 = 0
c_3 = 0
for _ in range(n):
    tmp = input()
    for i in range(len(tmp)-1):
        if tmp[i:i+2] ==  'AB':
            ans += 1
    if tmp[0] == 'B' and tmp[-1] == 'A':
        c_1 += 1
    elif tmp[0] == 'B':
        c_2 += 1
    elif tmp[-1] == 'A':
        c_3 += 1
if c_1 == 0:
    ans += min(c_2,c_3)
else:
    if c_2 + c_3 > 0:
        ans += c_1 + min(c_2,c_3)
    else:
        ans += c_1 - 1
print(ans)
