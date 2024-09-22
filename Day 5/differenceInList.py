l1 = [1,2,3]
l2 = [2,4,6]


# l1 = [1,2,3,3]
# l2 = [1,1,2,2]

l1 = set(l1)
l2 = set(l2)


l1 = list(l1)
l2 = list(l2)


ans1=[]
ans2=[]

for x in l1:
    if l2.count(x)>0:
        pass
    else:
        ans1.append(x)


for x in l2:
    if l1.count(x)>0:
        pass
    else:
        ans2.append(x)


print(ans1,ans2)