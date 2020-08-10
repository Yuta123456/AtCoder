def searchMax(array):
    max = array[0]
    Index = 0
    maxIndex = 0
    for i in array:
        if i > max:
            max = i
            maxIndex = Index
        Index += 1
    array.pop(maxIndex)
    return max

cardNum = int(input())
list = [int(i) for i in input().split()]
alice = 0
bob = 0
for i in range(cardNum):
    if i % 2 == 0:
        alice += searchMax(list)
    else:
        bob += searchMax(list)

print(alice - bob)
