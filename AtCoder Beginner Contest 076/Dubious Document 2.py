s = input()
t = input()
index = 0
s = ''.join(list(reversed(s)))
t = ''.join(list(reversed(t)))
#まず、？とtの統合性が取れているかを確認
#後ろから調べてく
exit_flag = True
for i in range(len(s)):
    if s[i] == t[0] or s[i] == '?':
        if i + len(t) >= len(s):
            break
        for j in range(len(t)):
            if not (s[i + j] == t[j] or s[i + j] == '?'):
                break
            if j == len(t) - 1:
                start_index = i
                exit_flag = False
        if not exit_flag:
            break
#条件に合わなかったら終わり

if exit_flag:
    print("UNRESTORABLE")
    exit()
ans = s[:start_index] + t + s[start_index + len(t):]
ans = ''.join(list(reversed(ans)))
ans = ans.replace("?", "a")
print(ans)
