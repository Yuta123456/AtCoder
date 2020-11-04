
N = int(input())
prime = []
sum_a = (2 * N - 1 + 1) * N / 2 
for i in range(2, int(sum_a**0.5) + 1):
    if sum_a % i == 0:
        prime.append([i, int(sum_a // i)])
array = [2*i+1 for i in range(N)]
for num, length in prime:
    if length < 2 * N - 1:
        continue
    else:
        # もう組める。
        use_num = set()
        row, column = num, N // num
        if (column % row) % 2 != 0:
            continue
        else:
            finish = N - (column % row)
            ans = [[] for i in range(row)]
            index = 0
            cnt = 0
            for i in range(row):
                for j in range(i, finish, row+1):
                    ans[i].append(array[j])
                    cnt += 1
            start = 1
            while cnt < N:
                start = 1 - start
                if start:
                    for i in range(row):
                        if cnt >= N:
                            break
                        ans[index].append(array[cnt])
                        cnt += 1
                        index += 1
                        index %= row
                else:
                    for i in range(row-1,-1,-1):
                        if cnt >= N:
                            break
                        ans[index].append(array[cnt])
                        cnt += 1
                        index += 1
                        index %= row
            print(num)
            for i in range(len(ans)):
                print(num, end=" ")
                print(sum(ans[i]) == length)
                for j in range(len(ans[i])):
                    print(ans[i][j],  end=" ")
                print()
            exit()
            
            
            
