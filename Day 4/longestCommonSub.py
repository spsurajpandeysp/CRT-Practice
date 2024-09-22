l=[2,6,1,9,4,5,3]
# l= [1,9,3,10,4,20,2]
l = sorted(l)
import math

count = 1

maxi = 0

for i in range(1,len(l)):
    if(l[i-1]+1==l[i]):
        count=count+1
        maxi = max(maxi,count)

    else:
        count=1

print(maxi)

