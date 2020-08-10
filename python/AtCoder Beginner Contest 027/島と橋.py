n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
ans = 0
if sum_a % n != 0:
    ans = -1
else:
    average = sum_a//n
    #つながっている島の数
    start_island = 0
    while start_island < n:
        if a[start_island] != average:
            count = 1
            total_people = a[start_island]
            while total_people / count != average:
                total_people += a[start_island + count]
                count += 1
            ans += (count - 1)
            start_island += count
        else:
            start_island += 1
print(ans)



