n, k = map(int, input().split())
s = input()
pre = 0
sepS = []
happyCount = 0
RLcount = 0
for i in range(1, n):
    if s[i] == s[i - 1]:
        happyCount += 1
    if s[i] == 'L' and s[i - 1] == 'R':
        RLcount += 1
#print("now HP =>{}".format(happyCount))
happyCount += min(k, RLcount) * 2
if k > RLcount:
    happyCount += 1
print(min(n - 1, happyCount))
