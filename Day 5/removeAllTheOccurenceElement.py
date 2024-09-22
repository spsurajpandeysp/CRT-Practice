# l = [1,2,2,3,4,2]
# n=2
# for x in l:
#     l.remove(n)

# print(l)


l = [1,2,2,3,4,2]
count=0

for x in l:
    count+=1


print(count)
j=count-1
i=0
while(i<count):
    if(l[i]==2):
        l[i],l[j] = l[j],l[i]
        j=j-1
    else:
        i=i+1

print(l)



print(l[count-i:count])





