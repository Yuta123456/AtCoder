n, m = list(map(int, input().split()))
card = list(map(int, input().split()))
data = []
for i in range(m):
    data.append(list(map(int, input().split())))
data.sort(key=lambda x:x[1])
data.reverse()
card.sort()
total = 0
k = 0
for i in range(m):
    s = min(data[i][0] - 1,len(card) - 1)
    if card[s] < data[i][1]:
        total += (s + 1)* data[i][1]
        card = card[s+1:]
    else:
        for j in range(min(data[i][0] ,len(card))):
            if card[j] < data[i][1]:
                total += data[i][1]
                k = j
            else:
                k = j - 1
                break
        card = card[k+1:]
total += sum(card)
print(total)
