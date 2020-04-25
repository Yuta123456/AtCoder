s = input()
p = s.replace('x', '')
k = [p[i] for i in range(len(p)-1,-1,-1)]
k = "".join(k)
if k == p:
    left = 0
    right = len(s)-1
    ans = 0
    while True:
        if s[left] != s[right]:
            if s[left] == 'x':
                left += 1
                ans += 1
            else:
                right -= 1 
                ans += 1
        else:
            right -= 1
            left += 1
        if right <= left:
            break
    print(ans)
else:
    print(-1)
