n = int(input())
b_sum = 0
data = []
for i in range(n):
    a, b = map(int, input().split())
    b_sum += b
    data.append(a + b)
data = sorted(data, reverse = True)
print(sum(data[0:n:2]) - b_sum)