n, k, c = map(int, input().split())
s = input()
fastest_schedule = [None for i in range(n)]
latest_schedule = [None for i in range(n)]
count = 1
last_workday = -10**10
for i in range(n):
    if s[i] == 'o' and i - last_workday > c:
        fastest_schedule[i] = count
        last_workday = i
        if count < k:
            count += 1
        else:
            break
count = k
last_workday = 10**18
for i in range(n-1,-1,-1):
    if s[i] == 'o' and last_workday - i > c:
        latest_schedule[i] = count
        last_workday = i
        if count > 1:
            count -= 1
        else:
            break

for i in range(n):
    if fastest_schedule[i] == latest_schedule[i] and fastest_schedule[i] != None:
        print(i+1)
    