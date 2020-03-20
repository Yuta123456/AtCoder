a = input()
b = input()
c = input()
ans = min(len(a), len(b), len(c))
#長さnの文字列s
#s[i:j]のハッシュ値:
#(hash1[j]-hash1[i]*power1[j-i]%mod1)%mod1
#((hash1[j]-hash1[i]*power1[j-i]%mod1)%mod1)*(10**10) + (hash2[j]-hash2[i]*power2[j-i]%mod2)%mod2

base1 = 1007
mod1 = 10**9+7

hash_a = [0]*(len(a)+1)
power_a = [1]*(len(a)+1)

hash_b = [0]*(len(b)+1)
power_b = [1]*(len(b)+1)

hash_c = [0]*(len(c)+1)
power_c = [1]*(len(c)+1)

for i,e in enumerate(a):
    hash_a[i+1] = (hash_a[i]*base1 + ord(e))%mod1
    power_a[i+1] = (power_a[i]*base1)%mod1
for i,e in enumerate(b):
    hash_b[i+1] = (hash_b[i]*base1 + ord(e))%mod1
    power_b[i+1] = (power_b[i]*base1)%mod1
for i,e in enumerate(c):
    hash_c[i+1] = (hash_c[i]*base1 + ord(e))%mod1
    power_c[i+1] = (power_c[i]*base1)%mod1
# a b c
