x = input()
ans = 0
s_count = 0
for i in range(len(x)):
    if x[i] == 'S':
        s_count += 1
    else:
        if s_count > 0:
            ans += 1
            s_count -= 1
print(len(x) - ans*2)