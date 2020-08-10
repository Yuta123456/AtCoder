n,l = map(int, input().split())
amida = []
for i in range(l):
    amida.append(list(input()))
y = list(input())
now = 0
for i in range(len(y)):
    if y[i] == "o":
        now = i
        break
amida.reverse()
for i in range(len(amida)):
    if amida[i][now-1] == '-':
        now -= 2
    elif now < n*2 - 2 and amida[i][now+1] == '-':
        now += 2
print((now//2) + 1)