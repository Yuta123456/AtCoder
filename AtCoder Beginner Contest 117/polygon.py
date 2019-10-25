n = int(input())
L = list(map(int, input().split()))
L.sort()
L.reverse()
if L[0] < sum(L[1:n]):
  print("Yes")
else:
  print("No")
