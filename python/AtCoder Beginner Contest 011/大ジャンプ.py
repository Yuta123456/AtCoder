import math
def combi(x, y):
    if x < y:
        return 0
    if (x,y) in memo:
        return memo[(x,y)]
    else:
        memo[(x,y)]  = math.factorial(x) / (math.factorial(x - y) * math.factorial(y))
        return memo[(x,y)]
memo = dict()
n, d = map(int, input().split())
x,y = map(int, input().split())
#可能かどうかの判定
if (x % d != 0 and x != 0) or (y % d != 0 and y == 0):
    print(0)
    exit()
#動かなきゃいけない最低の回数
x_move_count = abs(x // d)
y_move_count = abs(y // d)
if x_move_count + y_move_count > n or (n - (x_move_count + y_move_count)) % 2 != 0:
    print(0)
    exit()
count = 0
remain = n - (x_move_count + y_move_count)
remain //= 2
#n->残りの回数
for x_move in range(0,remain+1):
    p_x = x_move_count + x_move
    n_x = x_move
    p_y = y_move_count + (remain - x_move)
    n_y = (remain - x_move)
    count += math.factorial(n) // (math.factorial(p_x) * math.factorial(p_y) * math.factorial(n_x) * math.factorial(n_y))
print(count/pow(4,n))
#8 10000000 -40000000 -40000000

