n = int(input())
weekday = [
"Sun",
"Mon",
"Tue",
"Wed",
"Thu",
"Fri",
"Sat"]
for _ in range(n):
    s = input()
    for j in range(7):
        if weekday[j] == s:
            print(weekday[(j+1)%7])
