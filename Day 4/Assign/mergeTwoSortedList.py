l1= [ 25,34,35,78]
l2= [ 14,20,60,79]


i = 0
j = 0

ans = []

while i<len(l1) and j<len(l2):
    if l1[i]<=l2[j]:
        
        ans.append(l1[i])
        i+=1
    else:
        ans.append(l2[j])
        j+=1


while(i<len(l1)):
    
    ans.append(l1[i]) 
    i+=1


while(j<len(l2)):
    
    ans.append(l2[j])
    j+=1



print(ans)