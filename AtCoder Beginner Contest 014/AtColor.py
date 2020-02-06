n = int(input())
s = [0 for i in range(10**7+1)]
for i in range(n):
    a, b = map(int, input().split())
    s[a] += 1
    s[b+1] -= 1
for i in range(1,len(s)):
    s[i] += s[i-1]
print(max(s))