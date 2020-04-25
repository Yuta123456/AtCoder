n = list(input())
n.reverse()
odd = 0
even = 0
for i in range(len(n)):
    if i % 2 == 0:
        odd += int(n[i])
    else:
        even += int(n[i])
print("{} {}".format(even,odd))

