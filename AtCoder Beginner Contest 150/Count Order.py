import itertools
n = int(input())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
k = list(itertools.permutations(range(1,n+1), n))
ans_1 = 0
ans_2 = 0
for i in range(len(k)):
    if k[i] == a:
        ans_1 = i
    if k[i] == b:
        ans_2 = i
print(abs(ans_1 - ans_2))


