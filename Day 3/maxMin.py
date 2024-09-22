# find min and max

l = eval(input("Enter lIst: "))
max = min = l[0]

for x in range(1,len(l)):
  if(max<l[x]):
    max=l[x]
  if(min>l[x]):
    min=l[x]


  


print("Maximum Element is:",max)
print("Min Element is:",min)
