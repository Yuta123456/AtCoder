import collections
n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
now=0
for i in range(n*2):
    ans.append(a[now])
    now=a[now]-1
#print(ans)

#変更
passed = set()
ac = -1
for i in range(len(ans)):
    if ans[i] in passed:
        ac = ans[i]
        break
    else:
        passed.add(ans[i])
#print(ac)
index=-1
index2=-1

for i in range(len(ans)):
    if ans[i]==ac:
        if index==-1:        
            index=i
        else:
            index2=i
#print(index,index2)
#print((k-index-1)%(index2-index))
#print(ans)
if k < index:
    print(ans[k])
else:
    k -= (index + 1)
    ans = ans[index:]
    print(ans[k % (index2 - index)])

