s = input()
t = input()
data1 = [[0] for i in range(2)]
data2 = [[0] for i in range(2)]
for i in range(len(s)):
    if s[i] in data1[0]:
        if not data1[1][data1[0].index(s[i])] == t[i]:
            print("No")
            exit()
    else:
        data1[0].append(s[i])
        data1[1].append(t[i])

for i in range(len(s)):
    if t[i] in data2[0]:
        if not data2[1][data2[0].index(t[i])] == s[i]:
            print("No")
            exit()
    else:
        data2[1].append(s[i])
        data2[0].append(t[i])
print("Yes")
