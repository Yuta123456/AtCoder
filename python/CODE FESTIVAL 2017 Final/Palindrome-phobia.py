from collections import Counter
s = input()
n = len(s)
count = [0 for i in range(3)]
for i in range(n):
    count[ord(s[i]) - ord('a')] += 1
count.sort()
if count[2] - count[0] > 1:
    print("NO")
else:
    print("YES")