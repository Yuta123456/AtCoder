s = list(input())
ans = 0
b_count = 0
w_count = 0
#B, W の転倒数を数える
for i in range(len(s)):
    if s[i] == 'B':
        b_count += 1
    else:
        w_count += 1
        ans += b_count
print(ans)
