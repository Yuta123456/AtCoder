s = input()
t = input()
atcoder = set(["a","t","c","o","d","e","r"])
for i in range(len(s)):
    if s[i] != t[i]:
        if s[i] == t[i] == '@':
            continue
        elif s[i] == "@" and t[i] in atcoder:
            continue
        elif t[i] == "@" and s[i] in atcoder:
            continue
        print("You will lose")
        exit()
print("You can win")
