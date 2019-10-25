n = int(input())
s = input()
L = [0 for j in range(n)] # L[j] => W
R = [0 for j in range(n)]
if s[0] == "W":
    L[0] = 1
if s[-1] == "W":
    R[-1] = 1
for i in range(1,n):
    L[i] = L[i - 1]
    R[-(i + 1)] = R[-i]
    if s[i] == "W":
        L[i] += 1
    if s[-(i + 1)] == "W":
        R[-(i + 1)] += + 1
m = min(n - 1 - R[1], L[-2])
for i in range(1,n - 1):
    k = L[i- 1] + (n - i - 1) - R[i + 1]
    if m > k:
        m = k
print(m)
