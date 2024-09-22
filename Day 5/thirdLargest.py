l1 = 0
l2 = 0
l3 = 0


l = [3,8,1,10,5,9]

for x in l:
    if x>l1:
        l3 = l2
        l2 = l1
        l1 = x
    elif x>l2:
        l3 = l2
        l2 = x

    elif x>l3:
        l3 = x

print(l3)