data = []
for i in range(5):
    data.append(int(input()))
k = int(input())
data.sort()
if data[4] - data[0] > k:
    print(":(")
else:
    print("Yay!")
