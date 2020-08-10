a = 0
b = 0
q = 0
ans = 0
s = input()
n = len(s)
for i in range(n):
    if s[i] == 'A':
        a += 1
    elif s[i] == 'B':
        b += 1
    else:
        ans += a*b*(q+1)+a*(q+1)*q+(b+q-a)*q*(q+1)/2 -q*(2*q+1)*(q+1)/6
        print(ans)
        if s[i] == '?':
            q += 1
print(ans)
        