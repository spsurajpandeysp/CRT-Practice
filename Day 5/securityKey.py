n=578378923

freq = [0,0,0,0,0,0,0,0,0,0]

while(n>0):
    last = n%10
    freq[last]+=1
    n=n//10
 


ans=0
for i in freq:
    if i>=2:
        ans=ans+1
print(ans)