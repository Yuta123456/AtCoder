c = int(input())
baggage = []
for i in range(c):
    baggage.append(sorted(list(map(int, input().split()))))
a = max([baggage[i][0] for i in range(c)])
b = max([baggage[i][1] for i in range(c)])
d = max([baggage[i][2] for i in range(c)])
print(a*b*d)