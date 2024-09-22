l1= [98,35,34,35,35]
l2= [98,34,34,35,98]
ans=[]
for x in l1:
    if (l2.count(x)):
        l1.remove(x)
        l2.remove(x)
        ans.append(x)
print(ans)