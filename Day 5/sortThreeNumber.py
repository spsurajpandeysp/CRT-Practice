l = [2, 0, 1, 2, 1, 0]


i=0
j=0
k=len(l)-1

while(j<k):
    if(l[j]==1):
        j+=1
    if(l[j]==0):
        l[i],l[j] = l[j],l[i]
        j=j+1
        i=i+1
    if(l[j]==2):
        l[j],l[k] = l[k],l[j]
        k=k-1


print(l)