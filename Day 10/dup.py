ans = []


l = [1,3,1,2,3]

for x in l:
    if l.count(x)>1:
        if ans.count(x)==0:
            ans.append(x)



if len(ans)==0:
    print(-1)
else:
    print(ans)