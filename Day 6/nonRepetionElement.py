l = [1,1,2,3,2,1,4,5]

ans=[]

for x in l:
    if ans.count(x):
        ans.remove(x)
        ans.append(x)
    else:
        ans.append(x)

print(ans[0])


