l = [1,4,2,3,6,7,8]

i = 0

while(i<len(l)):
    mini = 1000000001
    j = i
    ind = i
    while(j<len(l)):
        if(mini>l[j]):
            ind = j
            mini = l[j]
        j=j+1

    l[i],l[ind]  = l[ind],l[i]
    i=i+1


print(l)