s = input()
n = len(s)
s = list(s.replace('BC','D'))
a_count = 0
ans = 0
i = 0
while i < len(s) - 1 :
    if s[i:i+2] == ['A','D']:
        ans += a_count + 1
        s[i+1] = 'A'
        s[i] = 'D'
    else:
        if s[i] == 'A':
            a_count += 1
        else:
            a_count = 0
    i += 1
print(ans)