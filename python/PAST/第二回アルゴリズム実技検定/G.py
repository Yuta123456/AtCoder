q = int(input())
data = []
index = 0
for i in range(q):
    query = list(input().split())
    query_kind = query[0]
    if query_kind == '1':
        data.append([query[1], int(query[2])])
    else:
        delete_cnt = 0
        word = [0 for i in range(26)]
        need_delete = int(query[1])
        while delete_cnt < need_delete:
            if index >= len(data):
                break
            if delete_cnt + data[index][1] > need_delete:
                data[index][1] -= need_delete - delete_cnt
                word[ord(data[index][0]) - ord('a')] += (need_delete - delete_cnt)
                break
            else:
                word[ord(data[index][0]) - ord('a')] += data[index][1]
                delete_cnt += data[index][1]
                index += 1
        ans = 0
        for i in range(26):
            ans += pow(word[i],2)
        print(ans)
            

