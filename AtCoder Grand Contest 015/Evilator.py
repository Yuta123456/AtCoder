s = input()
l = len(s)
ans = 0
for i in range(l):
    if s[i] == 'U':
        #go down => 2, up => 1
        ans += (i * 2) + (l - 1 - i)
    else:
        #go down => 1, up => 2
        ans += (l - 1 - i) * 2 + i
print(ans)
