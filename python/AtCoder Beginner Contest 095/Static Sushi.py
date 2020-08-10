memo = dict()
n,c = map(int, input().split())
data = []
data.append([0,0])
for i in range(n):
    data.append(list(map(int, input().split())))
start_to_a = [0 for i in range(n+1)]
value_sum = 0
for i in range(n+1):
    value_sum += data[i][1]
    start_to_a[i] = value_sum - data[i][0]
    if start_to_a[i] in memo:
        memo[start_to_a[i]] = min(memo[start_to_a[i]], data[i][0])
    else:
        memo[start_to_a[i]] = data[i][0]
good_end_a_for_b = [0 for i in range(n+1)]
for i in range(1,n+1):
    good_end_a_for_b[i] = max(good_end_a_for_b[i-1], start_to_a[i-1])
good_end_a_for_b[0] = max(start_to_a)
#good_end_a_for_b[i] := 終了がiの時、最適に選んだAの時のvalue
end_at_b = [0 for i in range(n+1)]
value_sum = 0
for i in range(n,-1,-1):
    value_sum += data[i][1]
    end_at_b[i] = value_sum - (c - data[i][0])
ans = 0
end_at_b[0] = 0
print(end_at_b)
#print(good_end_a_for_b)
for end in range(n+1):
    #前者は、O -> A -> B
    #後者は  O -> B -> A
    if end == 77:
        k = memo[good_end_a_for_b[end]]
        print("end at:{}, to a:{} gea:{} endatb:{}".format(end,k,good_end_a_for_b[end],end_at_b[end]))
        print(c-data[77][0])
        ans = max(ans, good_end_a_for_b[end] + end_at_b[end] - k, end_at_b[end] - (c - data[end][0]) + good_end_a_for_b[end])
        print(ans)
        print()
#O->Aの時
print(ans)