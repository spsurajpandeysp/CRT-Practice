l =[10,11,7,12,14]

sum=0

for i in range(0,len(l)-1):
    sum+=abs(l[i]-l[i+1])


print(sum)