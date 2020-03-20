n = int(input())
s = []
ans = 0
fin_with_a = 0
start_with_b = 0
for _ in range(n):
    tmp = input()
    s.append(tmp[0]+tmp[-1])
    for i in range(len(tmp)-1):
        if tmp[i:i+2] ==  'AB':
            ans += 1
print(s)
print(ans)
