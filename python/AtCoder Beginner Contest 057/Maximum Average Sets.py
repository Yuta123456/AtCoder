import math
n, a, b = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)
dict_num = dict()
def combi(x, y):
    return math.factorial(x) / (math.factorial(x - y) * math.factorial(y))
for i in v:
    if i in dict_num:
        dict_num[i] += 1
    else:
        dict_num[i] = 1
ans = 0
ans_max = 0.0
for i in range(a,b+1):
    k = v[:i]
    ans_max = max(ans_max, sum(k) / i)
for i in range(a,b+1):
    k = v[:i]
    if ans_max == (sum(k) / i) :
        p = 1
        index = 0
        while index < len(k):
            count = 1
            while index + 1 < len(k) and k[index] == k[index + 1]:
                count += 1
                index += 1
            p *= combi(dict_num[k[index]], count)
            index += 1
        ans += p
print(ans_max)
print(int(ans))