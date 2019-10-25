n = int(input())
red = []
blue = []
for i in range(n):
    red.append(list(map(int, input().split())))
for i in range(n):
    blue.append(list(map(int, input().split())))
red.sort()
blue.sort()
count = 0
print(red)
print(blue)
for i in range(n):
    for j in range(n):




print(count)
