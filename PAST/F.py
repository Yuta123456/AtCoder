s = input()
k = []
preindex = 0
for i in range(1,len(s)):
    if s[i] == s[i].upper():
        if preindex > i - 1:
            continue
        else:
            k.append(s[preindex:i+1])
            preindex = i+1
k.sort(key = lambda x:x.lower())
for i in range(len(k)):
    print("".join(k[i]), end="")
print()