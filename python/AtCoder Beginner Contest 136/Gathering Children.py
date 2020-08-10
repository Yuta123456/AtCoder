s = input()
data = []
target = 'LR'
pre = 0
for i in range(len(s) - 1):
    if s[i:i+2] == target:
        data.append(s[pre:i+1])
        pre = i + 1

data.append(s[pre:len(s)])
ans = []
for i in range(len(data)):
    ans.append([0] * len(data[i]))
target = 'RL'
for i in range(len(data)):
    for j in range(len(data[i]) - 1):
        if data[i][j:j+2] == target:
            if len(data[i]) % 2 == 0:
                ans[i][j] = len(data[i]) // 2
                ans[i][j + 1] = len(data[i]) // 2
                break
            else:
                if j % 2 == 0:
                    ans[i][j] = (len(data[i]) + 1 ) // 2
                    ans[i][j + 1] = len(data[i]) // 2
                else:
                    ans[i][j + 1] = (len(data[i]) + 1 ) // 2
                    ans[i][j] = len(data[i]) // 2
                break
for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j], end = " ")
