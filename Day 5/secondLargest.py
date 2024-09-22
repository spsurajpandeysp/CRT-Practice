l1 = 0
l2 = 0


l = [3,8,1,10,9]

for x in l:
    if x>l1:
        l2 = l1
        l1 = x
    elif l2<x:
        l2 = x

print(l2)