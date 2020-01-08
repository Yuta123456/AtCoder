import itertools
n = int(input())
t = []
mod = 7 + 10**9
def permutation_mod(n):
    permu_list = [0 for i in range(n+1)]
    permu_list[0] = 1
    permu_list[1] = 1
    for i in range(2,n+1):
        permu_list[i] = (permu_list[i-1] * i) % mod
    return permu_list

for i in range(n):
    t.append(int(input()))
ans_count = 1
t.sort()
acc = list(itertools.accumulate(t))
print(sum(acc))
num_change = 1
num_change_list = []
for i in range(n-1):
    if t[i] != t[i+1]:
        num_change_list.append(num_change)
        num_change = 0
    num_change += 1
num_change_list.append(num_change)
per_list = permutation_mod(max(num_change_list))
for i in num_change_list:
    ans_count *= per_list[i]
    ans_count %= mod
print(ans_count)

