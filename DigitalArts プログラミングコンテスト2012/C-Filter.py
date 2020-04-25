import re
s = input()
s = list(s.split())
n = int(input())
data = []
for _ in range(n):
    data.append(input())
for word in s:
    flag = True
    for ng in data:
        if len(word) != len(ng):
            continue
        else:
            same = True
            for i in range(len(word)):
                if word[i] != ng[i] and ng[i] != '*':
                    same = False
            if same:
                flag = False
    if flag:
        print(word, end=" ")
    else:
        print('*'*len(word), end=" ")
print()