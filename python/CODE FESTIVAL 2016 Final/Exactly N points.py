n = int(input())
total = 0
ng_number = -1
end_number = -1
for i in range(1, n + 1):
    total += i
    if total == n:
        end_number = i
        break
    elif total > n:
        ng_number = total - n
        end_number = i
        break
for i in range(1, n+1):
    if end_number < i:
        break
    if not ng_number == i:
        print(i)