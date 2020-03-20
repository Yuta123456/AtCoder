k = int(input())
#逆からシュミレートしていく
#これが、一番最後の形
array = [i for i in range(50)]
#50回単位で考えると、全ての要素が1増える操作となる
#つまり、k // 50を全てに足してあげるとほぼk回やった感じになる
plus = k // 50
rem = k % 50
for i in range(50):
    array[i] += plus
for i in range(rem):
    array[i] += 51
    for j in range(50):
        array[j] -= 1
print(50)
print(" ".join(map(str, array)))

