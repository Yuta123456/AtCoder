s = input()
k = int(input())
ans = 1
for i in range(len(s)):
    if s[i] != '1' and k > i:
        print(s[i])
        exit()
print(ans)
