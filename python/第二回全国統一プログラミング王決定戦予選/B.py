n = int(input())
d = list(map(int, input().split()))
mod = 998244353
distance_dict = {}
if d[0] != 0:
    print(0)
    exit()
for i in range(1,n):
    if d[i] == 0:
        print(0)
        exit()
    distance_dict[d[i]] = 0

for i in range(1,n):
    distance_dict[d[i]] += 1
pre = 1
ans = 1
for i in range(1,n):
    if i in distance_dict:
      ans *= pre ** distance_dict[i]
      pre = distance_dict[i]
      ans %= mod
      if i != 1 and i - 1 not in distance_dict:
          print(0)
          exit()
print(ans)