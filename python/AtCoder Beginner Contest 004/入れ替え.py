n = int(input())
k = n % 30
s = [1,2,3,4,5,6]
for i in range(k):
    s[i % 5], s[1 + i % 5] = s[1 + i % 5], s[i % 5]
ans = ""
for i in range(len(s)):
    ans += str(s[i])
print(ans)