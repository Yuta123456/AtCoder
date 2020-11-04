n = int(input())
ans = []
for i in range(1, int(pow(n, 0.5)) + 1):
    if n % i == 0:
        ans.append(i)
        ans.append(int(n//i))
ans = list(set(ans))
ans.sort()
for i in ans:
    print(i)
