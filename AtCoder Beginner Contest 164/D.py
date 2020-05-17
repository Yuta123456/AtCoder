s = input()
ans = 0
U = [0 for i in range(2019)]
mod = 2019
sum_i_to_n = 0
for i in range(len(s)-1,-1,-1):
    sum_i_to_n += int(s[i])* pow(10,len(s)-i-1,mod)
    sum_i_to_n %= mod
    if sum_i_to_n % mod == 0:
        ans += 1
    ans += U[sum_i_to_n]
    U[sum_i_to_n] += 1
print(ans)
