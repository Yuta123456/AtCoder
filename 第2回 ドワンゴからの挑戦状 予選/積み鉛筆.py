n = int(input())
k = list(map(int, input().split()))
k += [10**9]
ans = [k[0]]
for i in range(n-1):
    ans.append(min(k[i], k[i+1]))
print(" ".join(map(str, ans)))