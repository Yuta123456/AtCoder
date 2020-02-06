b = list(input())
num = dict()
for i in range(len(b)):
    num[b[i]] = i
n = int(input())
a = []
for i in range(n):
    a.append(input())
def rule(s):
    res = 0
    for i in range(len(s)):
        k = int(num[s[i]])
        res += k * (10 ** (len(s) - i - 1))
    return res
a.sort(key = rule)
for i in range(len(a)):
    print(a[i])
