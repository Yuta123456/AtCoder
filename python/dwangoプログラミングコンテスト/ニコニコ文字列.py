s = input()
count_25 = 0
index = 0
ans = 0
while index < len(s):
    if s[index:index+2] == '25':
        index += 2
        count_25 += 1
        ans += count_25
        continue
    else:
        count_25 = 0
    index += 1
print(ans)