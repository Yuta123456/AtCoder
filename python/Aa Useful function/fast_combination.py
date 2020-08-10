def mod_combination(n,k,mod):
    if k == 0:
        return 1
    return (n*mod_inv(k,mod) * mod_combination(n-1,k-1,mod) ) % mod
