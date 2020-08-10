n = int(input())
a = list(map(int, input().split()))
b = [0 for i in range(n)]
index = 0
count = 0
for i in range(n-1, -1, -1):
    if count % 2 == 0:
        b[index] = a[i]
        index += 1
    else:
        b[-index] = a[i]
    count += 1

print(" ".join(list(map(str, b)))) 

