n = int(input())
w = list(input().split())
w_to_n = dict()
w_to_n['b'] = '1'
w_to_n['c'] = '1'
w_to_n['t'] = '3'
w_to_n['j'] = '3'
w_to_n['l'] = '5'
w_to_n['v'] = '5'
w_to_n['p'] = '7'
w_to_n['m'] = '7'
w_to_n['n'] = '9'
w_to_n['g'] = '9'
w_to_n['d'] = '2'
w_to_n['w'] = '2'
w_to_n['f'] = '4'
w_to_n['q'] = '4'
w_to_n['s'] = '6'
w_to_n['x'] = '6'
w_to_n['h'] = '8'
w_to_n['k'] = '8'
w_to_n['z'] = '0'
w_to_n['r'] = '0'
ans = ''
for i in range(len(w)):
    p = ''
    for j in w[i]:
        if j.lower() in w_to_n:
            p += w_to_n[j.lower()] 
    if p:
        ans += (p + ' ')
print(ans[:-1])