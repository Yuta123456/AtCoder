n = int(input())
s = input()

sharp_list = [0 for i in range(n)]
dot_list = [0 for i in range(n)]

for i in range(n):
    if s[i] == '#':
        sharp_list[i] = sharp_list[i-1] + 1
    else:
        sharp_list[i] = sharp_list[i-1]

sharp_list = [0] + sharp_list

for i in range(n-1,-1,-1):
    if s[i] == '.':
        dot_list[i] = dot_list[(i+1)%n] + 1
    else:
        dot_list[i] = dot_list[(i+1)%n]
dot_list += [0]
ans = 10**9
for i in range(n+1):
    ans = min(sharp_list[i]+dot_list[i],ans)
print(ans)