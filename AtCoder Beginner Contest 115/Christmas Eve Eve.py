n = int(input())
p = [int(input()) for i in range(n)]
p.sort()
p.reverse()
p[0] = p[0] // 2
print(sum(p))
