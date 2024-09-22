l = [1,0,1,1,1,1,1,0,0,0,1]

maxi = 0
count = 0
for i in l:
  
    if i==1:
        count+=1
        maxi = max(count,maxi)
    else:
        count  = 0

print(maxi)