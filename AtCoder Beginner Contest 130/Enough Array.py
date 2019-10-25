n, k = list(map(int, input().split()))
data = list(map(int, input().split()))
count = 0
right = 0
left = 0
sum = 0
while right < n:
    if sum + data[right] < k:
        sum += data[right]
        right += 1
    else:
        count += (n - right)
        sum -= data[left]
        left += 1
print(count)
