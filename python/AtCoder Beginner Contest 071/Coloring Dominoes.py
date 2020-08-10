n = int(input())
s_1 = list(input())
s_2 = list(input())
array_kind = []
i = 0
while i < n:
    if s_1[i] == s_2[i]:
        array_kind.append('X')
        i += 1
    else:
        array_kind.append('Y')
        i += 2
ans = 1
mod = 10**9+7
if array_kind[0] == 'X':
    ans = 3
else:
    ans = 6
for i in range(1,len(array_kind)):
    if array_kind[i] == 'X':
        if array_kind[i-1] == 'X':
            ans *= 2
        else:
            ans *= 1
    else:
        if array_kind[i-1] == 'X':
            ans *= 2
        else:
            ans *= 3
    ans %= mod
print(ans)