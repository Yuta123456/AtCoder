from collections import Counter
s = input()
g_b = Counter(list(s))
c = g_b[s[0]]
for i in s:
    if c != g_b[i]:
        print("No")
        exit()
print("Yes")
    