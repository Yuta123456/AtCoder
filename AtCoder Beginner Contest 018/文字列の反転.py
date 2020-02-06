import copy
s = list(input())
n = int(input())
for i in range(n):
    l,r = map(int, input().split())
    k = copy.deepcopy(s[l-1:r])
    k.reverse()
    s = s[:l-1] + k + s[r:]
print("".join(s))
