import math
print("input k > ")
k = int(input())
real = 0
imag = 0
data1 = [1,1,0,0,-1,-1,0,0]
data2 = [1,0,-1,0,1,0,-1,0]
data = data2
#実部分
print()
for i in range(8):
    theta = ( 2 * math.pi * k * i ) / 8
    print("i = {} {}".format(i, data[i] * math.cos(theta)))
    print("i = {} {}".format(i, -data[i] * math.sin(theta)))
    print()
    real += data[i] * math.cos(theta)
    imag -= data[i] * math.sin(theta)  
print("{}+{}i".format(real, imag))
print("{}".format(math.sqrt(real * real + imag * imag)))