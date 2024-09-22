l = [[1,3],[2,6],[8,10],[15,18],[2,5]]



l = sorted(l)


last = l[0][1]
ans = []
ans.append(l[0])

for i in range(1,len(l)):
    temp = []
    if ans[i-1][1] <=l[i][0]:
        temp.append(l[0])
        temp.append(ans[i-1][0])
        ans.append(temp)
        
        ans.pop()

    else:
        ans.append(l[i])


print(ans)
        
    
