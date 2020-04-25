n = int(input())
ans_max = 0
ans_min = 0
d = []
for i in range(n):
    d.append(int(input()))
ans_max = sum(d)
if max(d)*2 - sum(d)<= 0:
    ans_min = 0
else:
    ans_min = max(d)*2 - sum(d)
print(ans_max)
print(ans_min)