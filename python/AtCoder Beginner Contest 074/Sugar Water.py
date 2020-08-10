a, b, c, d, e, f = list(map(int, input().split()))
a_count = 0
b_count = 0
c_count = 0
d_count = 0
max_per = 0.0
max_ans = [a*100,0]
while a_count * 100 * a <= f:
    b_count = 0
    c_count = 0
    d_count = 0
    while (a_count * a + b_count * b) * 100  <= f:
        c_count = 0
        d_count = 0
        while (a_count * a + b_count * b) * 100 + c_count * c <= f:
            d_count = 0
            while (a_count * a + b_count * b) * 100 + c_count * c + d_count * d <= f:
                #溶けてるのかどうか
                if (a_count * a + b_count * b)* e < (c_count * c + d_count * d):
                    break
                else:
                    if a_count + b_count + c_count + d_count == 0:
                        break
                    if max_per < (100 * (c_count * c + d_count * d) / ((a_count * a + b_count * b) * 100 + c_count * c + d_count * d)):
                        max_ans = [(a_count * a + b_count * b) * 100 + c_count*c + d_count*d, c_count*c + d_count * d]
                        max_per = (100 * (c_count * c + d_count * d) / ((a_count * a + b_count * b) * 100 + c_count * c + d_count * d))
                d_count += 1
            c_count += 1
        b_count += 1
    a_count += 1
print("{} {}".format(max_ans[0], max_ans[1]))