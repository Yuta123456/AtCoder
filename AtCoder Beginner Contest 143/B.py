n = int(input())
data = list(map(int, input().split()))
sum = 0
for i in range(n):
    for j in range(i+1, n):
        sum += data[i] * data[j]
print(sum)
