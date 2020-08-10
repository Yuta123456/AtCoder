n = input()
d = int(input())
l = len(n)
data = [0] * l
global total
total = 0
def search(data, k,d,l):
    global total
    if k == l:
        if sum(data) == d:
            total += 1
    else:
        for i in range(int(n[k]) + 1):
            data[k] = i
            print("data => {}\n k => {}\n d => {}\n l => {}\n \n".format(data,k,d,l))
            search(data, k + 1,d,l)
search(data,0,d,l)
print(total)
