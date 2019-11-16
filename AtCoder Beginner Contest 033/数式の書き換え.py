s = list(input())
preindex = 0
split_list = []
count = 0
for i in range(len(s)):
    if s[i] == '+':
        split_list.append(s[preindex:i])
        preindex = i + 1
split_list.append(s[preindex:])
for sl in split_list:
    if '0' not in sl:
        count += 1
print(count)