s = list(input())
pre_index = 0
split_s = []
for i in range(len(s) - 1):
    if s[i] == '>' and s[i + 1] == '<':
        split_s.append(s[pre_index:i+1])
        pre_index = i + 1
split_s.append(s[pre_index:])
ans = 0
for i in range(len(split_s)):
    l = split_s[i].count('<')
    r = split_s[i].count('>')
    if l > r:
        ans += sum(range(1,l+1))
        ans += sum(range(1,r))
    else:
        ans += sum(range(1,r+1))
        ans += sum(range(1,l))
print(ans)