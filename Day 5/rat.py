r=7
unit=2
n=8
arr = [2,8,3,5,7,4,1,2]

mul = r*unit

sum = 0
if(len(arr)==0):
    ans=-1
else:
    ans=0

for i in arr:
    sum +=i
    if(sum>=mul):
        ans=arr.index(i)+1
        break

if(mul==0):
    ans=0

print(ans)