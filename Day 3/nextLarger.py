n=5
l=[1,3,2,4,4]

ans=[]

for i in range(n):
  flag=0
  for j in range(i+1,n):
    if(l[i]<l[j]):
      ans.append(l[j])
      flag=1
      break


  if(flag==0):
      ans.append(-1)
  
      
print(ans)