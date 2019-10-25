n = int(input())
dic = {}
count = 0
for i in range(n):
    s = input()
    s = ''.join(sorted(list(s)))
    if s in dic:
        count += dic[s]
        dic[s] += 1
    else:
        dic[s] = 1
print(count)
