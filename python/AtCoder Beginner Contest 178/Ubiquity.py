n = int(input())
mod = 10**9 + 7
contain_zero = 0
contain_nine = 0
not_contain_zero_and_nine = 0
all_per = pow(10,n,mod)
if n < 2:
    print(0)
else:
    contain_zero = all_per - pow(9,n,mod)
    contain_nine = all_per - pow(9,n,mod)
    not_contain_zero_and_nine = pow(8,n,mod)
    print((-(all_per - not_contain_zero_and_nine -contain_nine - contain_zero))%mod)
    
