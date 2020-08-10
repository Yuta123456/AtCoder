s = input()
n = len(s)
for l in range(n):
    for r in range(n):
        ans = s[:l] + s[r:]
        if ans == 'keyence':
            print("YES")
            exit()
print("NO")