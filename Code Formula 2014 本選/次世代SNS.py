s = list(input().split())
ans = set()
for word in s:
    flag = False
    add = ""
    max_len = ""
    for j in range(len(word)):
        if word[j] == '@':
            if not flag:
                flag = True
            else:
                ans.add(add[1:])
                add = ""
        if flag:
            add += word[j]
    if len(max_len) < len(add):
        max_len = add
    ans.add(max_len[1:])
ans = list(ans)
ans.sort()
for i in range(len(ans)):
    if ans[i] != '':
        print(ans[i])

