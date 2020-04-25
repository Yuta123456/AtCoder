n = int(input())
c = input()
word = ['A','B','X','Y']
ans = 10**9
for one in word:
    for two in word:
        for three in word:
            for four in word:
                q = one + two
                r = three + four
                first = c.replace(q,'L')
                first = first.replace(r,'R')
                second = c.replace(r,'L')
                second = first.replace(q, 'R')
                ans = min(len(first), len(second), ans)
print(ans)