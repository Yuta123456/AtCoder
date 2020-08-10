a = input()
n = len(a)
ans =  n * (n-1) // 2
char = [0 for i in range(26)]
for i in range(n):
    char[ord(a[i])-ord('a')] += 1
for i in range(26):
    ans -= (char[i] * (char[i]-1))//2
print(ans+1)

