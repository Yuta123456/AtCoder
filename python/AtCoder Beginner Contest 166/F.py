n,a,b,c = map(int, input().split())
ans = []
number = dict()
number['A'] = a
number['B'] = b
number['C'] = c
query = [input() for i in range(n)]
for i in range(n):
    s = query[i]
    s_1, s_2 = s[0], s[1]
    if number[s_1] == 0 and number[s_2] == 0:
        print("No")
        exit()
    else:
        if number[s_1] > number[s_2]:
            number[s_1] -= 1
            number[s_2] += 1
            ans.append(s_2)
        elif number[s_1] < number[s_2]:
            number[s_2] -= 1
            number[s_1] += 1
            ans.append(s_1)
        else:
            if i == n-1:
                number[s_2] -= 1
                number[s_1] += 1
                ans.append(s_1)
            else:
                if query[i+1] == s_1 + s_2:
                    number[s_2] -= 1
                    number[s_1] += 1
                    ans.append(s_1)
                else:
                    n_1,n_2 = query[i+1]
                    if s_1 in set([n_1,n_2]):
                        number[s_2] -= 1
                        number[s_1] += 1
                        ans.append(s_1)
                    else:
                        number[s_1] -= 1
                        number[s_2] += 1
                        ans.append(s_2)

    #print("A:{} B:{} C:{}".format(number['A'],number['B'],number['C']))
print("Yes")
for i in range(n):
    print(ans[i])