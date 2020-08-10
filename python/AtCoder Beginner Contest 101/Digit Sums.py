n = input()
k = map(int, list(n))
if int(n) % sum(k) == 0:
    print("Yes")
else:
    print("No")
