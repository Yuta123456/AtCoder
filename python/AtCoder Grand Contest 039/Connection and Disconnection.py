s = list(input())
k = int(input())
ans = 0
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        ans += count//2
        count = 1
ans += count//2
if len(set(s)) == 1:
    print(len(s)*k//2)
    exit()
if s[0] != s[-1]:
    ans *= k
else:
    left = 0
    right = 0
    index = 0
    while index < len(s) and s[0] == s[index]:
        left += 1
        index += 1
    index = len(s)-1
    while index >= 0 and s[-1] == s[index]:
        right += 1
        index -= 1
    ans *= k
    ans -= ((right//2) + (left//2) - (right + left)//2) * (k-1)
print(ans)