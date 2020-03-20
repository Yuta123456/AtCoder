s = list(input())
q = set(list(s))
alpha = set([chr(i+ord('a')) for i in range(26)])
if alpha - q:
    use = alpha - q
    use = list(use)
    use.sort()
    print("".join(s) + use[0])
    exit()
for i in range(len(s)-1,-1,-1):
    asc = ord(s[i])
    q = set(s[:i+1])
    for j in range(asc,ord('z')+1):
        if chr(j) not in q:
            s[i] = chr(j)
            print("".join(s[:i+1]))
            exit()
print(-1)
