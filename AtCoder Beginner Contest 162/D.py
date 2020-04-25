n = int(input())
s = input()
count =[[0 for i in range(3)] for i in range(n+1)]
for i in range(1,n+1):
    if s[i-1] == 'R':
        count[i][0] = count[i-1][0] + 1
    else:
        count[i][0] = count[i-1][0]
    if s[i-1] == 'G':
        count[i][1] = count[i-1][1] + 1
    else:
        count[i][1] = count[i-1][1]
    if s[i-1] == 'B':
        count[i][2] = count[i-1][2] + 1
    else:
        count[i][2] = count[i-1][2]
ans = 0
words = set(['R','G','B'])
for i in range(n):
    for j in range(i+1,n):
        k = set([s[i],s[j]])
        if len(k) == 2:
            remain = (words - k)
            remain = list(remain)[0]
            d = j-i
            if remain == 'R':
                if j + d < n and s[j + d] == 'R':
                    ans += count[-1][0] - count[j][0] - 1
                else:
                    ans += count[-1][0] - count[j][0]
            elif remain == 'G':
                if j + d < n and s[j + d] == 'G':
                    ans += count[-1][1] - count[j][1] - 1
                else:
                    ans += count[-1][1] - count[j][1]
            else:
                if j + d < n and s[j + d] == 'B':
                    ans += count[-1][2] - count[j][2] - 1
                else:
                    ans += count[-1][2] - count[j][2]
print(ans)

