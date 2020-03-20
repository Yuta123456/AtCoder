import collections
n = int(input())
s = []
for i in range(n):
    s.append(input())
s = collections.Counter(s)
ans = []
k = list(s.most_common())
k_len = k[0][1]
for i in k:
    word, count = i
    if count == k_len:
        ans.append(word)
ans.sort()
for i in ans:
    print(i)