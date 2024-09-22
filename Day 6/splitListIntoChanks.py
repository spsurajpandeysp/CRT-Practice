l = [1,2,3,4,5,6,7,8]
chunks = 3

count = 0

temp=[]
ans=[]

for i in l:
    temp.append(i)
    count=count+1
    if(count==chunks):
        ans.append(temp)
        count=0
        temp=[]


if(len(temp)>0):
    ans.append(temp)


print(ans)