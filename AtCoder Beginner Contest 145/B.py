n = int(input())
n = n//2
s = list(input())
if s[:n] == s[n:]:
    print("Yes")
    exit()
print("No")