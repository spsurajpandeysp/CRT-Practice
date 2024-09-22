# l = eval(input("Enter number"))
l=[-1,2,-3,4,5,-6]

ans = 0

pos = []
neg = []

for x in l:
    if(int(x)>=0):
        pos.append(int(x))
    else:
        neg.append(int(x))

ans=[]

i = 0
j=0
k=0





while(k < len(pos) and j<len(neg)):
    if(i%2==0):
        ans.append(neg[j])
        j=j+1
    else:
        ans.append(pos[k])
        k=k+1

    i=i+1


while(k!=len(pos)):
    ans.append(pos[k])
    k=k+1

while(j!=len(neg)):
    ans.append(neg[j])
    j=j+1


print(ans)