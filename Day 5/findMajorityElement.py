l = [3,3,4,2,4,2,4,2,4,4]
l = sorted(l)
n=len(l)
print(l)
ans = []
i = 1
count=1
prevMax = 0
while(i<len(l)):
    if l[i]==l[i-1]:
        count+=1
    else:
        if(count>=n//2):
            ans.append(l[i])
        count=1
    i=i+1


if(count>=n//2):
    ans.append(l[len(l)-1])

print(ans)



