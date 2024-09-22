l=[1,4,5,3,2]
n=10

l = sorted(l)

ans=[]
i=1
for x in range(1,n+1):
    if l.count(x)==0:
        ans.append(x)


print(ans)